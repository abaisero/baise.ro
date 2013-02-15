from django.db import models

class Document(models.Model):
    name=models.CharField(max_length=100)
    doc=models.FileField(upload_to="documents/")

    def __unicode__(self):
        return self.name
