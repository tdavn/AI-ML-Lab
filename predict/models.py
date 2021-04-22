from django.db import models

# Create your models here.


class Classification(models.Model):

    keyword_1 = models.CharField(max_length=255)
    keyword_2 = models.CharField(max_length=255)
    keyword_3 = models.CharField(max_length=255)
    sentiment = models.CharField(max_length=255)

    def __str__(self):
        return self.sentiment
