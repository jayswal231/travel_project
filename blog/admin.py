from django.contrib import admin
from .models import *
# Register your models here.
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(Category)

class postadmin(SummernoteModelAdmin):
    # displaying posts with title slug and created time
    summernote_fields = ('post_content', )
    
admin.site.register(Post,postadmin)

admin.site.register([PostView,UrlView])
