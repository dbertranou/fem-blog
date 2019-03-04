from django.shortcuts import render
from django.http import Http404
from . models import Post, Category
from femblog.settings import POSTS_PER_PAGE


def index(request):
    ctx = {}
    content = {}
    content['latest_posts'] = Post.objects.all()[:POSTS_PER_PAGE]
    content['category_posts'] = [{
        'category': cat,
        'posts': Post.objects.filter(category=cat)[:POSTS_PER_PAGE]}
        for cat in Category.objects.all()]
    ctx['content'] = content
    return render(request, 'blog/index.html', ctx)


def category_posts(request, name):
    ctx = {}
    content = {}
    try:
        category = Category.objects.get(name=name)
    except Category.DoesNotExist:
        raise Http404('Not Found')
    content['category'] = category
    content['posts'] = Post.objects.filter(category=category)
    ctx['content'] = content
    return render(request, 'blog/results.html', ctx)
