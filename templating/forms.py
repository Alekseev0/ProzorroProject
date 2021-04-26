from django import forms


class TenderSearchForm(forms.Form):

    tender_hash = forms.CharField()
