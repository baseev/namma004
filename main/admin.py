from django.contrib import admin
from main.models import PostType, UserProfile, UserScore

# Admin Views
class PostTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')


# Added to Admin View
admin.site.register(PostType, PostTypeAdmin)
admin.site.register(UserScore)
admin.site.register(UserProfile)

