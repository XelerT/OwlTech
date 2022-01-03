from django.shortcuts import render
from .models import Article
# Create your views here.

def fizmat_un(request):
   news = Article.objects.order_by('date')
   return render(request, 'fizmat/fizmat_un.html', {'news':news})
