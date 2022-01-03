from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from .forms import ArticleForm
from django.views.generic import DetailView

# Create your views here.

def News(request):
    News = Article.objects.order_by('date')
    return render(request, 'News/News.html', {'News': News})

class NewsDetailView(DetailView):
    model = Article
    template_name = 'news/details_view.html'
    context_object_name = 'article'

def Create(request):
    form = ArticleForm()
    error = ''
    data = {
        'error': error,
        'form': form
    }
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Invalid data'
    return render(request, 'News/create.html', data)
