from django.shortcuts import render,render_to_response
from .forms import CurrencyConverterForm
from django.views.decorators.csrf import csrf_protect , requires_csrf_token , csrf_exempt
import requests

@csrf_exempt
def index(request) :
    form = CurrencyConverterForm(request.POST or None)
    if form.is_valid():
        fromC = form.cleaned_data.get("currency1")
        toC = form.cleaned_data.get("currency2")
        a  = form.cleaned_data.get("amount")
        response = requests.get('http://api.fixer.io/latest?symbols='+fromC+','+toC)
        theAnswer = response.json()
        if toC == 'EUR' or fromC == 'EUR' :
            theAnswer['rates']['EUR'] = 1
        returner = float(a)*(theAnswer['rates'][toC]/theAnswer['rates'][fromC])
        answer = a + ' ' + fromC +' = ' + str(returner)+' '+toC
        return render_to_response('index.html', {'form': form , 'answer' : answer })
    return  render_to_response('index.html',{'form' : form})
# Create your views here.
