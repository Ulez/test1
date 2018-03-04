from django.contrib import admin

# Register your models here.
from .models import *
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','btitle','bpub_date']#定义显示的内容；
    search_fields = ['btitle']
admin.site.register(BookInfo,BookInfoAdmin) #规定每一行的显示内容；
admin.site.register(HeroInfo)