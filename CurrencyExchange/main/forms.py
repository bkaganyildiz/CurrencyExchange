from django import forms
import requests
def getCurrencyChoices():
    response = requests.get('http://api.fixer.io/latest')
    currencies = response.json()
    returner =[]
    returner.append((currencies['base'],currencies['base']))
    for cur in currencies['rates'] :
        returner.append((cur,cur))
    return returner
class CurrencyConverterForm(forms.Form) :
    currency1 = forms.ChoiceField(required=True,label="From Currency")
    currency2 = forms.ChoiceField(required=True, label="To Currency")
    amount    = forms.CharField(widget=forms.TextInput(attrs={'type':'number'}))
    def __init__(self, *args, **kwargs):
        super(CurrencyConverterForm, self).__init__(*args, **kwargs)
        self.fields['currency1'].choices = getCurrencyChoices()
        self.fields['currency2'].choices = getCurrencyChoices()