from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Classification


# Create your views here.
def predict(request):
    return render(request, 'classifier.html')


def predict_chances(request):

    if request.POST.get('action') == 'post':

        # Receive data from client
        key1 = request.POST.get('key1')
        key2 = request.POST.get('key2')
        key3 = request.POST.get('key3')

        # tweet pull-down
        import tweepy as tw
        import pandas as pd

        ACCESS_TOKEN = '917808967274741762-r8YbHiXfNrUXJXn1dubUchtWrOZ2DMk'
        ACCESS_TOKEN_SECRET = 'jWo0gkDV5VGzaBkDeAkYc1e3dzf4D7N5IpuV6QdjR9x5E'
        CONSUMER_API_KEY = 'QaEAZ16UhHcc33CiZ6y8b672n'
        CONSUMER_API_SECRET = 'EIwXgXYGFBYZbMqTt22byRnQiQuUfWKqxbM03KKCiCTXiE8tVA'
        auth = tw.OAuthHandler(CONSUMER_API_KEY, CONSUMER_API_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        api = tw.API(auth)

        # define search settings
        search_words = key1
        for kw in [key2, key3]:
            if kw.strip():
                search_words += f' OR ({kw.strip()})'

        tweet_search = search_words + ' -filter:retweets AND filter:replies'
        tweets = tw.Cursor(api.search, q=tweet_search, count=10, lang='en').items(100)

        # Create dataframe
        tweet_component = []
        for tweet in tweets:
            tweet_component.append([tweet.user.id, tweet.created_at, tweet.user.screen_name, tweet.user.location, tweet.text.encode('utf-8')])
            df_tweet = pd.DataFrame(tweet_component, columns=['ID', 'Time', 'User name', 'Location', 'Text'])

        # Pre-processing
        import numpy as np
        import nltk
        from nltk.corpus import stopwords
        import re
        import string

        def data_cleaner(tweet):
            # lower text
            tweet = tweet.lower()
            # remove urls
            tweet = re.sub(r'http\S+', ' ', str(tweet))
            # remove html tags
            tweet = re.sub(r'<.*?>',' ', tweet)
            # remove tweets containing digits
            tweet = re.sub('\w*\d\w*', ' ', tweet)
            # remove hashtags
            tweet = re.sub(r'#\w+',' ', tweet)
            # remove mentions
            tweet = re.sub(r'@\w+',' ', tweet)
            # remove anything not a letter
            tweet = re.sub(r'\W+', ' ', tweet)
            tweet = tweet.strip()
            #removing words with length less than 2 or in stop words
            tweet = tweet.split()
            tweet = [w for w in tweet if len(w)>1]
            tweet = " ".join([word for word in tweet if not word in stop_words])
            return tweet

        stop_words = stopwords.words('english')

        df_tweet['cleaned_tweet'] = df_tweet['Text'].apply(data_cleaner)

        # Drop nan in cleaned_tweet column
        df_tweet.replace('', np.nan, inplace=True)
        df_tweet = df_tweet.dropna(subset=['cleaned_tweet'])

        df_tweet = df_tweet[['User name', 'Time', 'Location', 'cleaned_tweet']]

        # Load the model
        import joblib
        model = joblib.load('tfidf_rf_pipeline.sav')
        df_tweet['labels'] = df_tweet['cleaned_tweet'].apply(lambda x: model.predict([x])[0])

        # classification
        def sentiment_class(df):
            if df['labels'].value_counts()[1]/len(df) >= 0.8:
                return 'Highly favor!'
            elif (df['labels'].value_counts()[1]/len(df) >= 0.6) & (df['labels'].value_counts()[1]/len(df) < 0.8):
                return 'Recommend!'
            elif (df['labels'].value_counts()[1]/len(df) >= 0.4) & (df['labels'].value_counts()[1]/len(df) < 0.6):
                return 'Normal Quality.'
            else: return 'Not recommend!'

        final = sentiment_class(df_tweet)

        # create model objects that are defined in models.py
        Classification.objects.create(keyword_1=key1, keyword_2=key2, keyword_3=key3, sentiment=final)

        return JsonResponse({'sentiment': final, 'primary_keyword': key1, 'secondary_keyword': key2, 'third_keyword': key3}, safe=False)  # sent back to the classifier.html -> see javascript part


def view_results(request):
    # Submit prediction and show all
    data = {"dataset": Classification.objects.all()}
    return render(request, "results.html", data)
