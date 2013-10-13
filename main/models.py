from django.db import models
from django.contrib.auth.models import User
import datetime



class PostType(models.Model):
    name            = models.CharField(max_length=250)
    created         = models.DateTimeField(default=None)
    updated         = models.DateTimeField(default=datetime.datetime.now())
    deleted_flag    = models.SmallIntegerField(default=0)
    
    def __unicode__(self):
        return self.name
    

class UserScore(models.Model):
    user           = models.ForeignKey(User) 
    score          = models.IntegerField(default=0)
    created        = models.DateTimeField(default=None)
    updated        = models.DateTimeField(default=datetime.datetime.now())
    deleted_flag   = models.SmallIntegerField(default=0)

#     def __unicode__(self):
#         return self.user.join(" - ").join(self.score)


