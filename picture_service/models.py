from django.db import models


class Image(models.Model):
    id = models.IntegerField(primary_key=True)
    image = models.ImageField(upload_to='images', default='media/default.png')
    alt = models.CharField(max_length=500)

    def __str__(self):
        return self.alt
