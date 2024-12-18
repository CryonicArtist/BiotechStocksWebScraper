import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define function to scrape a website
def scrape_news(stock_symbol):
    url = f"https://news.example.com/search?q={stock_symbol}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract news headlines, summaries, and links
    articles = []
    for item in soup.find_all('div', class_='news-item'):
        headline = item.find('h2').text
        summary = item.find('p').text
        link = item.find('a')['href']
        date = item.find('span', class_='date').text
        articles.append({'headline': headline, 'summary': summary, 'link': link, 'date': date})

    return pd.DataFrame(articles)

# Example usage
biotech_stocks = ['AMGN', 'BIIB', 'VRTX']
for stock in biotech_stocks:
    news = scrape_news(stock)
    news.to_csv(f'{stock}_news.csv', index=False)