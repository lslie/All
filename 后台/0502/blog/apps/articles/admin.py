from django.contrib import admin
from .models import Category,ArticleInfo,TagInfo

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','add_time']


class ArticleInfoAdmin(admin.ModelAdmin):
    list_display = ['name','author','desc','content','label','click_num','love_num','image','add_time','is_delete']

class TagInfoAdmin(admin.ModelAdmin):
    list_display = ['name','add_time']


admin.site.register(Category,CategoryAdmin)
admin.site.register(ArticleInfo,ArticleInfoAdmin)
admin.site.register(TagInfo,TagInfoAdmin)