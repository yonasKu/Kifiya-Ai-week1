import pandas as pd
from textblob import TextBlob
from sklearn.feature_extraction.text import CountVectorizer

def sentiment_analysis(df, headline_column):
    def get_sentiment(text):
        analysis = TextBlob(text)
        return analysis.sentiment.polarity  # Returns a value between -1 and 1

    df['sentiment'] = df[headline_column].apply(get_sentiment)
    return df['sentiment'].describe()

def topic_modeling(df, headline_column, num_topics=5):
    vectorizer = CountVectorizer(stop_words='english', max_features=5000)
    X = vectorizer.fit_transform(df[headline_column])
    
    # Top words (as a proxy for topic modeling)
    word_counts = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())
    top_words = word_counts.sum().sort_values(ascending=False).head(num_topics)
    
    return top_words
