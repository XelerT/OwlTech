from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def func(request):
   return render(request, 'main/func.html')

def Extention(request):
   return render(request, 'main/SameHTML.html')

def test(request):
   return HttpResponse("<h4><font color=blue>QWERTY</font><h4>")


