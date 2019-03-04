from django.shortcuts import render
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


def categories(request, name):
    posts = Post.objects.filter(
        category__name__icontains=name).order_by('-published')
    return render(request, 'blog/results.html', {'posts': posts})
