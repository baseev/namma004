from django.contrib import admin
from kisaa.models import PostType, UserPost


# Admin Views
class PostTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')
 
class UserPostAdmin(admin.ModelAdmin):
    list_display = ('user', 'post_type', 'content')   

    

# Added to Admin View
admin.site.register(PostType, PostTypeAdmin)
admin.site.register(UserPost, UserPostAdmin)



