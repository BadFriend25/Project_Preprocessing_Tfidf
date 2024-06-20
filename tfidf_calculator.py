from sklearn.feature_extraction.text import TfidfVectorizer

def calculate_tfidf(articles):
    vectorizer = TfidfVectorizer(max_features=5000)
    tfidf_weights = vectorizer.fit_transform(articles)
    return tfidf_weights