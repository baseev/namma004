from django.contrib import admin
from activity.models import UserPost, UserComment, UserPostLike, UserCommentLike, SpamComment, SpamPost

# Admin Views 
class UserPostAdmin(admin.ModelAdmin):
    list_display = ('user', 'post_type', 'content')   


# Added to Admin View
admin.site.register(UserPost, UserPostAdmin)
admin.site.register(UserComment)
admin.site.register(UserPostLike)
admin.site.register(UserCommentLike)
admin.site.register(SpamComment)
admin.site.register(SpamPost)

