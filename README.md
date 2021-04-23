# AI-ML-Lab Project
### Motivation  
<p>BenchSci - a Toronto-based company uses data mining and AI plaforms to analyze the scientific data commercial information to aid researchers to decide on qualified biochemical reagents for their work.</p>
<h3> Ideas </h3>
<p>There are over one in five adults in US is active on Twitter. Twitter is the most popular plaform among scocial media networks that people used for exchange of public health information. </p>
<p>We may create a classifier that can collect and extract relevant information about a health-related product/serviceon in Twitter. </p>
<p>That would be a valuable reference for customers who want to know about that brand.</p>
<h3> Tasks</h3>
<ol>
<li> Use sentiment140 data set that contains tweets with sentiment categorized in positive or negative bins to train a classifier.</li>
<li> Use twitter api to create queries of a interested brand.</li>
<li> Use the classifier from (1) to understand the sentiment from the tweets from (2), which shows % of positive and negative evalutation.</li>
<li> Deploy the classifier on Django</li>
</ol>
<h3> Descriptions</h3>
<b>  This is a Django-based platform that integrate a ML classifier for tweet sentiment classification</b>
<b>  A Restful API is also included (Django REST Framework-DRF) for later scalability.</b>
<h3> Major features </h3>
<ol>
<li> Real-time tweet collection. On-the-fly analysis</li>
<li> ML-based classifier trained from Sentiment140 dataset</li>
<li> Powered by Django web framework in back-end. Responsive layout and mobile friendly front-end with the latest Bootstrap </li>
<li> Scalable and highly secured by DRF</li>
</ol>
<h3> Structure</h3>
<ul>
<li> Folder hompage: contain all code for the project.</li>
<li> ipynb files: python conde explanation in Jupyter Notebook</li>
<li> tfidf_rf_pipeline.sav: The saved classifier (saved with Joblib) for sentiment labelling</li>
<li> requirements.txt: contain information of dependencies</li>
</ul>