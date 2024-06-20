import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def calculate_tfidf(preprocessed_articles):
    vectorizer = TfidfVectorizer()
    tfidf_weights = vectorizer.fit_transform(preprocessed_articles)
    return tfidf_weights, vectorizer

def calculate_keyword_weights(tfidf_weights, vectorizer, articles):
    keyword_weights = {}
    for i, article in enumerate(articles):
        for word in article.split():
            if word not in keyword_weights:
                keyword_weights[word] = 0
            keyword_weights[word] += tfidf_weights[i, vectorizer.vocabulary_.get(word, 0)]
    return keyword_weights

# Example articles
articles = [
    "This is the first article. It's about machine learning.",
    "The second article is about natural language processing.",
    "The third article discusses the importance of keyword extraction."
]

# Preprocess the articles (e.g., tokenize, remove stop words, etc.)
preprocessed_articles = [' '.join(article.split()) for article in articles]

# Now you can call the functions
tfidf_weights, vectorizer = calculate_tfidf(preprocessed_articles)
keyword_weights = calculate_keyword_weights(tfidf_weights, vectorizer, preprocessed_articles)

# Print the keyword weights
print(keyword_weights)