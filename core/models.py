from django.db import models
# Create your models here.


class DBOject(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField()
    deleted_by = models.IntegerField()

    class Meta:
        abstract = True