# AI-ML-Lab Project
### Motivation  
BenchSci - a Toronto-based company uses data mining and AI plaforms to analyze the scientific data commercial information to aid researchers to decide on qualified biochemical reagents for their work.
### Ideas 
<p>There are over one in five adults in US is active on Twitter. Twitter is the most popular plaform among scocial media networks that people used for exchange of public health information. </p>
<p>We may create a classifier that can collect and extract relevant information about a health-related product/serviceon in Twitter. </p>
<p>That would be a valuable reference for customers who want to know about that brand.</p>
### Tasks
<ol>
<li> Use sentiment140 data set that contains tweets with sentiment categorized in positive or negative bins to train a classifier.</li>
<li> Use twitter api to create queries of a interested brand.</li>
<li> Use the classifier from (1) to understand the sentiment from the tweets from (2), which shows % of positive and negative evalutation.</li>
<li> Deploy the classifier on Django</li>
</ol>
### File structure
- Folder hompage: contain all code for the project.
- ipynb files: python conde explanation in Jupyter Notebook
- tfidf_rf_pipeline.sav: The saved classifier (saved with Joblib) for sentiment labelling
- requirements.txt: contain information of dependencies
