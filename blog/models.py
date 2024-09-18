from django.db import models
from django.conf import settings
from django.utils import timezone
from core.models import DBOject
import uuid
from django.urls import reverse


#Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return (super().get_queryset().filter(status=Post.Status.PUBLISHED))


class Post(DBOject):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    uuid = models.UUIDField(default=uuid.uuid4)
    slug = models.SlugField(max_length=250)
    title = models.CharField(max_length=250)
    body = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blog_posts'    
    )
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=2,
        choices=Status,
        default=Status.DRAFT
    )

    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.

    class Meta:
        ordering = ['-publish']
        indexes = [models.Index(fields=['-publish']),]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:show', args=[self.uuid])

class Comment(DBOject):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created']),
        ]
    def __str__(self):
        return f'Comment by {self.name} on {self.post}'


# class ORMPost(DBOject):
#     class Status(models.TextChoices):
#         DRAFT = 'DF', 'Draft'
#         PUBLISHED = 'PB', 'Published'

#     uuid = models.UUIDField(default=uuid4)
#     slug = models.SlugField(max_length=250)
#     title = models.CharField(max_length=250)
#     body = models.TextField()
#     author = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#         related_name='blog_posts'    
#     )
#     publish = models.DateTimeField(default=timezone.now)
#     status = models.CharField(
#         max_length=2,
#         choices=Status,
#         default=Status.DRAFT
#     )

#     class Meta:
#         ordering = ['-publish']
#         indexes = [models.Index(fields=['-publish']),]

#     def __str__(self):
#         return self.title