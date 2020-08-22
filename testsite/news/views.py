from django.shortcuts import render
from django.http import HttpResponse
from .models import News


def index(request):
    # print(request)
    # news = News.objects.all()
    # res = '<h1>Список новостей</h1>'
    # for item in news:
    #     res += f'<div>\n<p>{item.title}</p>\n<p>{item.content}</p>\n</div>\n<hr>\n'
    # return HttpResponse(res)
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей'
    }
    return render(request, template_name='news/index.html', context=context)

# def test(request):
#     return HttpResponse('<H1>Тестовая страница</H1>')
