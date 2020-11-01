from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import CommentForm
from django.urls import reverse
from django.http import Http404, HttpResponseRedirect


def index(request):
    latest_articles_list = Article.objects.order_by('-pub_date')[:5]
    return render(request, 'articles/list.html', {'latest_articles_list': latest_articles_list})


def detail(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Статья не найдена!")

    return render(request, 'articles/detail.html', {'article': a})


def leave_comment(request):
    error = ''
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('detail')
        else:
            error = 'Данные не заполнены'

    form = CommentForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'articles/detail.html', context)
