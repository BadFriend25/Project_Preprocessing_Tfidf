import requests
from bs4 import BeautifulSoup

def extract_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text()
    return text

def scrape_articles(website_url):
    article_links = []
    response = requests.get(website_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    for link in soup.find_all('a', class_='article-link'):
        article_links.append(link['href'])
    return article_links

def scrape_all_articles(website_urls):
    all_articles = []
    for website_url in website_urls:
        article_links = scrape_articles(website_url)
        for link in article_links:
            text = extract_text(link)
            all_articles.append(text)
    return all_articles