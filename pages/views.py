from django.shortcuts import render
from django.core.paginator import Paginator,InvalidPage,EmptyPage
from pages.models import Page

def pageView(request,page_name='home'):
    pages=Page.objects.all()
    page=pages.get(name=page_name)
    articles=page.article_set.all().order_by("-pub_date")
    paginator=Paginator(articles,5)
    # TODO modify num pages and what to do with first and last pages..
    try:
        pagenum=int(request.GET.get("p",'1'))
    except ValueError:
        pagenum=1

    try:
        articles=paginator.page(pagenum)
    except (InvalidPage,EmptyPage):
        articles=paginator.page(paginator.num_pages)

    context=dict(page_name=page_name,page=page,articles=articles,pages=pages)
    return render(request,'pages/page.html',context)
