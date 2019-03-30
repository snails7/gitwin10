# from django.shortcut import render

# Create your views here.

from django.http import HttpResponse

def book(request):
    return HttpResponse('图书首页')

def book_detail(request, book_id, category_id):
    # 可以从数据库中根据book_id提取这个图书的信息
    text = "您获取的图书id是： %s, category is: %s" % (book_id, category_id)
    return HttpResponse(text)


