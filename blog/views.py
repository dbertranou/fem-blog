from django.shortcuts import render
from . models import Post, Category


def index(request):
    ctx = {}
    content = {}
    content['latest_posts'] = Post.objects.all().order_by('-published')[:4]
    content['category_posts'] = [{
        'category': cat,
        'posts': Post.objects.filter(category=cat).order_by('-published')[:3]}
        for cat in Category.objects.all()]
    ctx['content'] = content
    return render(request, 'blog/index.html', ctx)


def categories(request, name):
    posts = Post.objects.filter(
        category__name__icontains=name).order_by('-published')
    return render(request, 'blog/results.html', {'posts': posts})
