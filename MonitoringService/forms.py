from django import forms



class TenderSearchForm(forms.Form):
    #Form that helps to get tender hash from search
    tender_hash = forms.CharField()
