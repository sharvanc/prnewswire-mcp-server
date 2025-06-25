import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime, timedelta


# getting links from prnewswire
def get_links_prnewswire(topic, num_days=7):
    '''
    This function fetches news article links from prnewswire based on the topic and date range.

    Args:
        topic (str): The topic to search for.
        num_days (int, optional): Number of days to fetch news from (counting back from today). 
        Default is 7 days.

    Returns:
        list: A list of news article links.
    '''
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=num_days)).strftime('%Y-%m-%d')
        
    session = requests.Session()
    url = f"https://www.prnewswire.com/search/news/?keyword={topic.replace(' ', '%20')}&page=1&pagesize=100"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = session.get(url, headers=headers)

    fetched_links = []

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        article_items = soup.find_all('div', class_='row newsCards')
        for item in article_items:
            article_age = item.find('h3').find('small').get_text(strip=True)
            article_link = item.find('a')
            if article_age and article_link:
                article_link_url = 'https://www.prnewswire.com' + article_link['href']
            
            article_date_str = ('').join(article_age.split(',')[:-1])
            if pd.to_datetime(start_date) <= pd.to_datetime(article_date_str) <= pd.to_datetime(end_date) and item['lang'].startswith('en'):
                fetched_links.append(article_link_url)
    else:
        print('Request failed with status code:', response.status_code)

    return list(set(fetched_links))


# getting the article content from prnewswire article link
def get_article_content(link):
    '''
    Fetches the content of a news article from PRNewswire.

    Args:
        link (str): The URL of the news article.

    Returns:
        dict: A dictionary containing the title, date, and content of the article.
    '''
    session = requests.Session()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = session.get(link, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        article = soup.find('article')
        if not article:
            print('No article found on the page:', link)
            return None
        # article title
        article_title = article.find('h1').get_text(strip=True)
        # article content
        paragraphs = article.find_all('p')
        article_date = paragraphs[0].get_text(strip=True)
        article_content = '\n'.join([p.get_text(strip=True) for p in paragraphs[2:-1]])

        return {
            'title': article_title,
            'date': article_date,
            'content': article_content
        }
    else:
        print('Failed to retrieve content from:', link)
        return None