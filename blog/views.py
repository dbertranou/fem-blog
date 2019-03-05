from django.shortcuts import render, get_object_or_404
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
    category = get_object_or_404(Category, name=name)
    content['category'] = category
    content['posts'] = Post.objects.filter(category=category)
    ctx['content'] = content
    return render(request, 'blog/results.html', ctx)


def posts(request):
    ctx = {}
    content = {}
    content['posts'] = Post.objects.all()
    ctx['content'] = content
    return render(request, 'blog/results.html', ctx)
