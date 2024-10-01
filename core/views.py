from django.shortcuts import render, get_object_or_404, redirect
from .models import News, Comment, Category, Author
from django.contrib.auth.decorators import login_required

def index(request):
    news_list = News.objects.all().select_related('category', 'author')
    return render(request, 'core/index.html', {'news_list': news_list})


def create_news(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        category_id = request.POST.get('category')
        author_id = request.POST.get('author')
        publication_date = request.POST.get('publication_date')
        publication_time = request.POST.get('publication_time')
        category = Category.objects.get(id=category_id)
        author = Author.objects.get(id=author_id)

        
        news = News(
            title=title,
            content=content,
            category=category,
            author=author,
            publication_date=publication_date if publication_date else None,
            publication_time=publication_time if publication_time else None
        )
        news.save()

        return redirect('index') 

    categories = Category.objects.all()
    authors = Author.objects.all()

    return render(request, 'core/create_news.html', {'categories': categories, 'authors': authors})


def update_news(request, news_id):
    news = get_object_or_404(News, id=news_id)

    if request.method == 'POST':
        news.title = request.POST.get('title')
        news.content = request.POST.get('content')
        category_id = request.POST.get('category')
        author_id = request.POST.get('author')

        news.category = Category.objects.get(id=category_id)
        news.author = Author.objects.get(id=author_id)

        news.save()

        return redirect('news_list') 
    categories = Category.objects.all()
    authors = Author.objects.all()

    return render(request, 'core/update_news.html', {'news': news, 'categories': categories, 'authors': authors})


def delete_news(request, news_id):
    news = get_object_or_404(News, id=news_id)
    
    if request.method == 'POST':
        news.delete()
        return redirect('index')
    
    return render(request, 'core/delete_news.html', {'news': news})

@login_required
def add_comment(request, news_id):
    news = get_object_or_404(News, id=news_id)

    if request.method == 'POST':
        content = request.POST.get('content')

        if content:
            Comment.objects.create(
                news=news,
                user=request.user,
                content=content
            )
            return redirect('news_detail', news_id=news.id)

    return render(request, 'core/add_comment.html', {'news': news})


def top_news(request):
    news = News.objects.order_by('-views')[:10]
    return render(request, 'core/top_news.html', {'news_list': news})