from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=52)
    
    def __str__(self):
        return self.name


class Post(models.Model):
    optionsEnum = (('draft', 'DRAFT'), ('published', 'PUBLISHED'))

    class Meta:
        ordering = ('-published', )

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')
        
    objects = models.Manager() # data from manager
    company = models.ForeignKey(Company, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=50)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=50, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_posts')
    status = models.CharField(max_length=10, choices=optionsEnum, default='published')
    postObj = PostObjects() # data from custom manager

    def __str__(self):
        return self.title



