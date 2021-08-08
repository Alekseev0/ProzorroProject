from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


class Tender(models.Model):
    """ Tender model """
    hash = models.TextField(unique=True)
    created_data = models.DateTimeField(auto_now=True)
    updated_data = models.DateTimeField(auto_now_add=True)
    title = models.TextField()
    data = models.JSONField()
    tender_start_date = models.DateTimeField(null=True)
    tender_end_date = models.DateTimeField(null=True)
    last_status = models.TextField(null=True)
    status_monitoring = models.BooleanField(default=True)


class SearchHistory(models.Model):
    """ Model used to save tenders, which were searched by user """
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    tender = models.ManyToManyField(Tender)






# Create your models here.
