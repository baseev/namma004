from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.


class CompanyProfile(models.Model):
    user            = models.ForeignKey(User)
    company_name    = models.CharField(max_length=250)
    last_nai      = models.CharField(max_length=250)
    created         = models.DateTimeField(default=None)
    updated         = models.DateTimeField(default=datetime.datetime.now())
    deleted_flag    = models.SmallIntegerField(default=0)

#     def __unicode__(self):
#         return self.user

