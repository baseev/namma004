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
    
#    
class UserPost(models.Model):
    content         = models.TextField()
    image           = models.ImageField(upload_to="images/posts/")
    user            = models.ForeignKey(User)
    post_type       = models.ForeignKey(PostType)
    created         = models.DateTimeField(default=None)
    updated         = models.DateTimeField(default=datetime.datetime.now())
    deleted_flag    = models.SmallIntegerField(default=0)

    def __unicode__(self):
        return self.content



class UserComment(models.Model):
    content         = models.TextField()
    post            = models.ForeignKey(UserPost)
    user            = models.ForeignKey(User)
    created         = models.DateTimeField(default=None)
    updated         = models.DateTimeField(default=datetime.datetime.now())
    deleted_flag    = models.SmallIntegerField(default=0)

    def __unicode__(self):
        return self.content



class UserPostLike(models.Model):
    post            = models.ForeignKey(UserPost)
    user            = models.ForeignKey(User)
    created         = models.DateTimeField(default=None)
    updated         = models.DateTimeField(default=datetime.datetime.now())
    deleted_flag    = models.SmallIntegerField(default=0)
    
#     def __unicode__(self):
#         return self.user.join(" - ").join(self.post)
    
    

class UserCommentLike(models.Model):
    comment         = models.ForeignKey(UserComment)
    user            = models.ForeignKey(User)
    created         = models.DateTimeField(default=None)
    updated         = models.DateTimeField(default=datetime.datetime.now())
    deleted_flag    = models.SmallIntegerField(default=0)

#     def __unicode__(self):
#         return self.user.join(" - ").join(self.comment)



class SpamComment(models.Model):
    comment         = models.ForeignKey(UserComment)
    marked_by       = models.ForeignKey(User)   
    created         = models.DateTimeField(default=None)
    updated         = models.DateTimeField(default=datetime.datetime.now())
    deleted_flag    = models.SmallIntegerField(default=0)

#     def __unicode__(self):
#         return self.marked_by.join(" - ").join(self.comment)


class SpamPost(models.Model):
    post            = models.ForeignKey(UserPost)
    marked_by       = models.ForeignKey(User)   
    created         = models.DateTimeField(default=None)
    updated         = models.DateTimeField(default=datetime.datetime.now())
    deleted_flag    = models.SmallIntegerField(default=0)

#     def __unicode__(self):
#         return self.marked_by.join(" - ").join(self.post)



class UserScore(models.Model):
    user           = models.ForeignKey(User) 
    score          = models.IntegerField(default=0)
    created        = models.DateTimeField(default=None)
    updated        = models.DateTimeField(default=datetime.datetime.now())
    deleted_flag   = models.SmallIntegerField(default=0)

#     def __unicode__(self):
#         return self.user.join(" - ").join(self.score)



class UserProfile(models.Model):
    user            = models.ForeignKey(User)
    first_name      = models.CharField(max_length=250)
    last_name       = models.CharField(max_length=250)
    created         = models.DateTimeField(default=None)
    updated         = models.DateTimeField(default=datetime.datetime.now())
    deleted_flag    = models.SmallIntegerField(default=0)

#     def __unicode__(self):
#         return self.user

