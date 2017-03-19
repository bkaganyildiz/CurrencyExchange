from django.shortcuts import render,render_to_response
from .forms import CurrencyConverterForm
from django.views.decorators.csrf import csrf_protect , requires_csrf_token , csrf_exempt

@csrf_exempt
def index(request) :
    form = CurrencyConverterForm(request.POST or None)
    if form.is_valid():
        pass
    return  render_to_response('index.html',{'form' : form})
# Create your views here.
