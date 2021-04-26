from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseBadRequest, Http404, HttpResponse
from templating.tender_service.tender_service import ProzorroTenderService
from .models import Tender
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


    def _tender_save_to_db(self, tender):
        if not tender:
            raise Http404
        tender = Tender(
            hash=tender.get('id', 'Empty'),
            data=tender,
            tender_start_date=tender.get('tenderPeriod', {}).get('startDate'),
            tender_end_date=tender.get('tenderPeriod', {}).get('endDate'),
            last_status=tender.get('status')
            )
        tender.save()
        return tender

    def post(self, request, *args, **kwargs):
        tender_hash = request.POST.get('tender_hash')
        if not tender_hash:
            return HttpResponseBadRequest()

        service = ProzorroTenderService()
        tender = service.get_tender(tender_hash)
        print(tender)
        if not tender or tender.get('status') == 'error':
            raise Http404

        qs_tender = self._tender_save_to_db(tender.get('data'))

        context = self.get_context_data(**kwargs)
        context['tender'] = qs_tender
        return self.render_to_response(context)





# Create your views here.
