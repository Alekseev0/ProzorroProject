from celery import shared_task
from django.core.mail import send_mail


#Mail for the tenders,that are not complete yet
def tender_changes_mail(username, tender_title, past_status, present_status, user_email):
    send_mail(
        'Tender monitoring service',
        f'Hello, {username} '
        f'Status of the tender {tender_title} was changed from {past_status} to '
        f'{present_status}. You may check it in your profile',
        'courseprojectdjango@gmail.com',
        [user_email],
        fail_silently=False
    )

#Mail for the tenders,that are complete
def tender_complete_mail(username, tender_title, status, user_email):
    send_mail(
        'Tender monitoring service',
        f'Hello, {username}. '
        f'Tender {tender_title} is {status}. You may check it in your profile',
        'courseprojectdjango@gmail.com',
        [user_email],
        fail_silently=False
    )


@shared_task
def check_tender():
    from MonitoringService.models import Tender, SearchHistory
    from datetime import datetime
    import pytz
    from MonitoringService.tender_service.tender_service import ProzorroTenderService

    #Function which updates tender information

    tenders = Tender.objects.all()
    service = ProzorroTenderService()
    now = datetime.now()
    now = pytz.utc.localize(now)
    for tender in tenders:
        try:
            if tender.tender_start_date < now:
                updated_tender = service.get_tender(tender.hash)
                updated_tender = updated_tender.get('data')
                tender.tender_start_date = updated_tender.get('tenderPeriod', {}).get('startDate')
                tender.tender_end_date = updated_tender.get('tenderPeriod', {}).get('endDate')
                tender.data = updated_tender
                if tender.last_status != updated_tender.get('status'):
                    for user_history in SearchHistory.objects.all().filter(tender=tender):
                        tender_changes_mail(
                            user_history.user.username,
                            tender.title,
                            tender.last_status,
                            updated_tender.get("status"),
                            user_history.user.email)
                tender.last_status = updated_tender.get('status')
                tender.updated_data = now
                tender.save()

        except TypeError:
            #If tender is already complete, then it`s start and end dates will be NoneType, and we will get TypeError
            if tender.last_status == 'complete' and tender.status_monitoring is True:
                tender.status_monitoring = False
                tender.save()
                for user_history in SearchHistory.objects.all().filter(tender=tender):
                    tender_complete_mail(user_history.user.username,
                                         tender.title,
                                         tender.last_status,
                                         user_history.user.email)











