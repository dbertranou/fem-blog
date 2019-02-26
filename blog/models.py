from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.username


class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    DRAFT = 'DR'
    PENDING = 'PE'
    PUBLISHED = 'PU'
    POST_STATE_CHOICES = (
        (DRAFT, 'Draft'),
        (PENDING, 'Pending'),
        (PUBLISHED, 'Published'),
    )

    title = models.CharField(max_length=100)
    summary = models.TextField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(null=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag)
    state = models.CharField(
        max_length=2, choices=POST_STATE_CHOICES, default=DRAFT)

    def __str__(self):
        return self.title
