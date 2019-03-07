from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Post, Category, Tag
from femblog.settings import POSTS_PER_PAGE


def index(request):
    ctx = {}
    ctx['latest_posts'] = Post.objects.all()[:POSTS_PER_PAGE]
    ctx['category_posts'] = [{
        'category': cat,
        'posts': Post.objects.filter(category=cat)[:POSTS_PER_PAGE]}
        for cat in Category.objects.all()]
    return render(request, 'blog/index.html', ctx)


def posts(request, category_name=None):
    ctx = {}
    criteria = {}
    title = 'Últimos posts'
    if category_name:
        category = get_object_or_404(Category, name=category_name)
        title = category.readable_name
        criteria['category'] = category
    ctx['posts'] = Post.objects.filter(**criteria)
    ctx['title'] = title
    return render(request, 'blog/results.html', ctx)


def post_detail(request, slug):
    ctx = {}
    post = get_object_or_404(Post, slug=slug)
    ctx['post'] = post
    return render(request, 'blog/detail.html', ctx)


def filter_list(request):
    response = {}
    response['categories'] = list(Category.objects.values())
    response['tags'] = list(Tag.objects.values())
    return JsonResponse(response)
