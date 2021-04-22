from django.db import models

class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)

# class Classification_record(models.Model):
#     search_keys = models.CharField(max_length=255)
#     sentiment = models.CharField(max_length=255)
#     search_date = models.DateField(auto_now_add=True)
#
#     def __str__(self):
#         return self.sentiment

class Sentiment_analysis(models.Model):
    search_keys = models.CharField(max_length=200)
    result = models.CharField(max_length=200)
    search_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.search_keys
