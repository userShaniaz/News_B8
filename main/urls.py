from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.views import index, create_news, update_news, delete_news, add_comment, top_news
from debug_toolbar import urls as debug_toolbar_urls

urlpatterns = [
    path('__debug__/', include(debug_toolbar_urls)),
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('create/', create_news, name='create_news'),
    path('update/<int:news_id>/', update_news, name='update_news'),
    path('delete/<int:news_id>/', delete_news, name='delete_news'),
    path('<int:news_id>/comment/', add_comment, name='add_comment'),
    path('top-news/', top_news, name='top_news'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)