from django.contrib import admin
from .models import Category, Article


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('creared_at', 'updated_at')
    search_fields = ('name', 'description')
    list_display = ('name', 'creared_at')

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'creared_at', 'updated_at')
    search_fields = ('title', 'content', 'user__username')
    list_display = ('title', 'public', 'user', 'creared_at')
    list_filter = ('public', 'user', 'categories')


    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id
        
        obj.save()

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)