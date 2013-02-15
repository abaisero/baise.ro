from django.db import models

class Page(models.Model):
    name=models.CharField(max_length=100,unique=True,help_text="The page textual ID. Must be unique.")
    title=models.CharField(max_length=100,help_text="Page title.")
    about=models.CharField(max_length=100,help_text="Short description.")
    pub_date=models.DateTimeField(auto_now_add=True,editable=False)
    is_blog=models.BooleanField(default=False,help_text="Select if the page should be formatted as a blog.")

    def __unicode__(self):
        return self.name

    def num_articles(self):
        return self.article_set.count()
