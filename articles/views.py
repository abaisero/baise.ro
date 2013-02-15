from django.shortcuts import render
from articles.models import Article

def articleView(request,article_id):
    article=articles.objects.get(id=article_id)
    context=dict(article=article)
    return render(request,'articles/article.html',context)
