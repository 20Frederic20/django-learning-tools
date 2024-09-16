from django.db import models
from django.conf import settings
from django.utils import timezone
from core.models import DBOject
from uuid import uuid4

#Create your models here.
class Post(DBOject):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    uuid = models.UUIDField(default=uuid4)
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

    class Meta:
        ordering = ['-publish']
        indexes = [models.Index(fields=['-publish']),]

    def __str__(self):
        return self.title

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