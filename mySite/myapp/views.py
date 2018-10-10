from django.shortcuts import render
from django.http.response import HttpResponse
from myapp.forms import KakikomiForm

# Create your views here.
def index_template(response):
    return render(request, 'index.html')

def kakikomi(request):
    f = KakikomiForm()
    return HttpResponse(f)
