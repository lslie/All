from django.shortcuts import render
from .models import ArticleInfo,TagInfo
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.


def article_next(request,sd_id):
    if sd_id:
        article = ArticleInfo.objects.filter(id=int(sd_id))[0]
    all_articles = ArticleInfo.objects.all()

    # 排行
    click_num = all_articles.order_by('-click_num')[:6]
    love_num = all_articles.order_by('-love_num')[:6]

    # 获取标签
    tag_all = TagInfo.objects.all()
    tagid = request.GET.get('tagid', '')
    # 归档
    date_time = all_articles.datetimes('add_time', 'day', order='DESC')
    year = request.GET.get('year', '')
    month = request.GET.get('month', '')
    day = request.GET.get('day', '')
    if year and month and day:
        all_articles = all_articles.filter(add_time__year=year, add_time__month=month, add_time__day=day)
        all_articles_set = set(all_articles)
    if tagid:
        tag = TagInfo.objects.filter(id=int(tagid))[0]
        all_articles = tag.article.all()
        all_articles_set1 = set(all_articles)
    try:
        a = list(all_articles_set & all_articles_set1)
        if a:
            all_articles = a
    except:
        pass

    # 分页
    pa = Paginator(all_articles, 2)
    page_num = request.GET.get('page_num', 1)
    try:
        pages = pa.page(page_num)
    except PageNotAnInteger:
        pages = pa.page(1)
    except EmptyPage:
        pages = pa.page(pa.num_pages)

    return render(request, 'article.html', {
        'article': article,
        'all_articles': pages,
        'click_num': click_num,
        'love_num': love_num,
        'tag_all': tag_all,
        'tagid': tagid,
        'date_time': date_time,
        'year': year,
        'month': month,
        'day': day,

    })
