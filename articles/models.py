from django.db import models
from django.conf import settings

from django.template.defaultfilters import slugify
import markdown

from pages.models import Page
from images.models import Image

class Article(models.Model):
    page=models.ForeignKey(Page,help_text="Page in which to publis the article.")
    title=models.CharField(max_length=100,help_text="Article title.")
    body=models.TextField(help_text="Article content.")
    pub_date=models.DateTimeField(auto_now_add=True,editable=False)
    images=models.ManyToManyField(Image,blank=True,help_text="Images contained in the article.")

    def __unicode__(self):
        return self.title

    def html(self):
        image_ref=""
        for image in self.images.all():
            image_url=settings.MEDIA_URL+image.image.url
            image_ref="%s\n[%s]: %s" % (image_ref,image.name,image_url)

        md="%s\n%s" % (self.body,image_ref)
        return markdown.markdown(md)
