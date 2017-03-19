from django.shortcuts import render,render_to_response
from .forms import CurrencyConverterForm

@csrf_exempt
def index(request) :
    form = CurrencyConverterForm(request.POST or None)
    if form.is_valid():

    return  None
# Create your views here.
