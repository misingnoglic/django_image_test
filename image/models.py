from django.db import models

# Create your models here.

class X(models.Model):
    image = models.ImageField(upload_to='mugshots/')
    name = models.CharField(max_length=10)
    def mugshot(self):
        return '<img width="300" src="%s"/>' % self.image.url
    mugshot.allow_tags = True

