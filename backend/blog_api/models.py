from django.db import models
from django.utils import timezone
from django.conf import settings


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Tag(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    tag = models.ForeignKey(Tag, on_delete=models.PROTECT, null=True, blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=127, unique_for_date='published_at')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    # Default Manager
    objects = models.Manager()
    # Custom Manager
    published = PublishedManager()

    class Meta:
        ordering = ('-published_at',)

    def __str__(self):
        return self.title
