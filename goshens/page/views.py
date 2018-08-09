from django.shortcuts import render, get_object_or_404
from .models import Page, Category


def page_list(request):
    categories = Category.objects.all()
    pages = Page.objects.all()
    return render(request, 'blog/post/index.html', {'categories': categories, 'pages': pages})


def index_list(request):
    categories = Category.objects.all()
    pages = Page.objects.all()
    return render(request, 'page/page_list.html', {'categories': categories, 'pages': pages})


def page_detail(request, id):
    page = get_object_or_404(Page, id=id)
    return render(request, 'page/page_detail.html', {'page': page})


def post_by_category(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    pages = Page.objects.filter(category__slug=category_slug)
    # print(category)
    return render(request, 'page/post_by_category.html', {'category': category, 'pages': pages})
