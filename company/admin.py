from django.contrib import admin
from company.models import CompanyProfile

# Admin Views
class PostTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')


# Added to Admin View
admin.site.register(CompanyProfile)

