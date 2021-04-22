from django.shortcuts import render
from django.http import HttpResponse
from .models import Greeting, Sentiment_analysis
from . import funct
from rest_framework import viewsets
from .serializers import SentimentSerializer

# Create your views here.
class SentimentView(viewsets.ModelViewSet):
    queryset = Sentiment_analysis.objects.all()
    serializer_class = SentimentSerializer

def manager(request):
    import json
    import requests
    api_request = requests.get('http://localhost:8000/demo/apiclassifier/')
    try:
        api = json.loads(api_request.content)
    except Exception as err:
        api = 'Error...'
    return render(request, 'manager.html', {'api':api})

def index(request):
    return render(request, "index.html")

def db(request):
    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()
    return render(request, "db.html", {"greetings": greetings})

def demo(request):
    keys = ''
    final = ''
    if request.method == 'POST':
        keys = request.POST['keywords']
        list_keys = keys.split(',')
        search_words = ' OR '.join([f'({x.strip()})' for x in list_keys])
        try:
            df_tweet = funct.create_tweet_df(search_words)
            # Load the model
            import joblib
            model = joblib.load('./tfidf_rf_pipeline.sav')
            df_tweet['labels'] = df_tweet['cleaned_tweet'].apply(lambda x: model.predict([x])[0])

            final = funct.sentiment_class(df_tweet)
            Sentiment_analysis.objects.create(search_keys=keys , result=final)
        except:
            final = 'No information found!'

    return render(request, "demo.html", {'result': final, 'search_keys': keys})
