from django.contrib import admin
from kisaa.models import PostType, UserPost, UserComment, UserPostLike, UserCommentLike, SpamComment, SpamPost, UserScore, UserProfile


# Admin Views
class PostTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')
 
class UserPostAdmin(admin.ModelAdmin):
    list_display = ('user', 'post_type', 'content')   

    

# Added to Admin View
admin.site.register(PostType, PostTypeAdmin)
admin.site.register(UserPost, UserPostAdmin)
admin.site.register(UserComment)
admin.site.register(UserPostLike)
admin.site.register(UserCommentLike)
admin.site.register(SpamComment)
admin.site.register(SpamPost)
admin.site.register(UserScore)
admin.site.register(UserProfile)

