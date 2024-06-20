import web_scraper
import preprocessor
import tfidf_calculator
import keyword_weight_calculator
import csv

def read_links_from_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        links = [row[0] for row in reader]
    return links

website_links_file = 'website_links.csv'
website_urls = read_links_from_csv(website_links_file)

all_articles = web_scraper.scrape_all_articles(website_urls)

preprocessed_articles = [preprocessor.preprocess_text(article) for article in all_articles]

tfidf_weights = tfidf_calculator.calculate_tfidf(preprocessed_articles)

keyword_weights = keyword_weight_calculator.calculate_keyword_weights(tfidf_weights, preprocessed_articles)

for word, weight in sorted(keyword_weights.items(), key=lambda x: x[1], reverse=True):
    print(f'{word}: {weight:.4f}')