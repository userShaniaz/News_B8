from django.contrib import admin
from .models import Category, Author, News, Comment


# class NewsAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'content', 'category', 'author', 'created_at', 'views')
#     list_display_links = ('id', 'title')
#     search_fields = ('title', 'content')
#     list_filter = ('category', 'author', 'created_at')

# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('id', 'news', 'user', 'content', 'created_at')
#     list_display_links = ('id', 'news', 'user')  
#     search_fields = ('news__title', 'content', 'user__username') 
#     list_filter = ('created_at', 'user')

admin.site.register(Category)
admin.site.register(Author)
admin.site.register(News)
admin.site.register(Comment)