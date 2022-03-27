from ctypes import HRESULT
from django.http import HttpResponse

def primer_vista(request):
    return  HttpResponse ("Hello word from my firt view in Django")
