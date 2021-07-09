from json import JSONDecodeError

from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.http import HttpResponseBadRequest, Http404
from django.db.models import F

from MonitoringService.tender_service.tender_service import ProzorroTenderService
from .models import Tender, SearchHistory
from .forms import TenderSearchForm


class TenderSearchView(TemplateView):
    template_name = 'tender_search.html'
    form_class = TenderSearchForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def _adding_tender_to_user_history(self, request, tender):
        #Uses to create object of UserHistory model
        if request.user.is_authenticated:
            try:
                user_history, existing_user = SearchHistory.objects.get_or_create(user=request.user)
                user_history.tender.add(tender)
                user_history.save()
            except TypeError:
                return tender

    def _saving_tender_and_history(self, request, tender):
        #Saving tender to database and calling function _adding_tender_to_user_history
        if not tender:
            raise Http404
        try:
            tender = Tender(
                hash=tender.get('id', 'Empty'),
                data=tender,
                title=tender.get('title', 'Not found'),
                tender_start_date=tender.get('tenderPeriod', {}).get('startDate'),
                tender_end_date=tender.get('tenderPeriod', {}).get('endDate'),
                last_status=tender.get('status')
                )
            tender.save()
            self._adding_tender_to_user_history(request, tender)
        except IntegrityError:
            existing_tender = Tender.objects.get(hash=tender.hash)
            self._adding_tender_to_user_history(request, existing_tender)
        return tender
    
    def post(self, request, *args, **kwargs):
        #Gets tender from Prozorro by received from form hash
        tender_hash = request.POST.get('tender_hash')
        if not tender_hash:
            return HttpResponseBadRequest()
        try:
            service = ProzorroTenderService()
            tender = service.get_tender(tender_hash)
        except JSONDecodeError:
            return redirect('/homepage/search/')
        if not tender or tender.get('status') == 'error':
            return redirect('/homepage/search/')
        
        qs_tender = self._saving_tender_and_history(request, tender.get('data'))

        context = self.get_context_data(**kwargs)
        context['tender'] = qs_tender
        return self.render_to_response(context)



class ProfileView(ListView):
    context_object_name = 'tenders'
    template_name = 'profile.html'
    paginate_by = 3

    def get_queryset(self):
        #Display user history of searched tenders in profile
        try:
            SearchHistory.objects.get(user=self.request.user)
            for user in SearchHistory.objects.all().filter(user=self.request.user):
                tenders = user.tender.all().order_by(F('tender_end_date').desc(nulls_last=True))
                return tenders
        except SearchHistory.DoesNotExist:
            return []

    def post(self, request, *args, **kwargs):
        #Allows user to remove tenders from his history in his profile
        for user_history in SearchHistory.objects.all().filter(user=self.request.user):
            user_history.tender.remove(self.request.POST.get('DeleteButton'))

        return redirect('/profile/')


def homepage(request):
    return render(request, 'about.html')


def redirection_to_homepage(request):
    return redirect('/homepage/')



