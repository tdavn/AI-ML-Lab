from rest_framework import serializers
from .models import Sentiment_analysis

class SentimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sentiment_analysis
        fields = ('id', 'search_date', 'search_keys', 'result')
