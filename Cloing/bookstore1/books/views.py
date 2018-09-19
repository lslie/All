from django.shortcuts import render,redirect
from books.models import Books
from books.enums import *
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    '''显示首页'''
    python_new = Books.object.get_books_by_type(PYTHON, 3, sort='new')
    python_hot = Books.object.get_books_by_type(PYTHON, 4, sort='hot')
    javascript_new = Books.object.get_books_by_type(JAVASCRIPT, 3, sort='new')
    javascript_hot = Books.object.get_books_by_type(JAVASCRIPT, 4, sort='hot')
    algorithms_new = Books.object.get_books_by_type(ALGORITHMS, 3, sort='new')
    algorithms_hot = Books.object.get_books_by_type(ALGORITHMS, 4, sort='new')
    machinelearning_new = Books.object.get_books_by_type(MACHINELEARNING, 3,sort='new')
    machinelearning_hot = Books.object.get_books_by_type(MACHINELEARNING, 4, sort='hot')
    operatingsystem_new = Books.object.get_books_by_type(OPERATINSGYSTEM, 3, sort='new')
    operatingsystem_hot = Books.object.get_books_by_type(OPERATINSGYSTEM, 4, sort='hot')
    database_new = Books.object.get_books_by_type(DATABASE, 3, sort='new')
    database_hot = Books.object.get_books_by_type(DATABASE, 4, sort='hot')

    # 定义模板上下文
    content = {
        'python_new': python_new,
        'python_hot': python_hot,
        'javascript_new': javascript_new,
        'javascript_hot': javascript_hot,
        'algorithms_new': algorithms_new,
        'algorithms_hot': algorithms_hot,
        'machinelearning_new': machinelearning_new,
        'machinelearning_hot': machinelearning_hot,
        'operatingsystem_new': operatingsystem_new,
        'operatingsystem_hot': operatingsystem_hot,
        'database_new': database_new,
        'database_hot': database_hot,
    }
    return render(request, 'index.html', content)


def deatil(request, books_id):
    '''显示商品的详细信息'''
    books = Books.object.get_books_by_id(books_id=books_id)

    if books is None:
        return redirect(reverse('index'))

    # 新品推荐
    books_li = Books.object.get_books_by_type(type_id=books.type_id, limit=2, sort='new')

    # 定义返回数据
    content = {
        'books': books,
        'books_li': books_li,
    }
    return render(request, 'detail.html', content)