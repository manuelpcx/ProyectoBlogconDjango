from django.shortcuts import render, get_object_or_404
from .models import Category, Article

# Create your views here.

def list(request):

    article = Article.objects.all()

    return render(request, 'articles/list.html', {
        'title': 'Articulos',
        'articles': article
    })

def category(request, category_id):

    category = get_object_or_404(Category, id=category_id)
    articles = Article.objects.filter(categories=category)

    return render(request, 'categories/category.html', {
        'category': category,
    })
