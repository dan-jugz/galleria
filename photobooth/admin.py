from django.contrib import admin
from .models import User,Image,tags

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)

admin.site.register(User)
admin.site.register(Image,ImageAdmin)
admin.site.register(tags)