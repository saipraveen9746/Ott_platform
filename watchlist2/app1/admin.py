from django.contrib import admin
from .models import Movies,Series
from django.contrib import admin
from embed_video.admin import AdminVideoMixin

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(Movies,MyModelAdmin)
admin.site.register(Series)



