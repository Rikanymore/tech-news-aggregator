import requests
from bs4 import BeautifulSoup
from datetime import datetime
from database.db import save_article
from database.models import Session
from config import SITES

def scrape_site(name, config):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(config['url'], headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = []
        
        for item in soup.select(config['selectors']['container'])[:5]:
            title = item.select_one(config['selectors']['title'])
            link = title.get('href') if title else None
            
            # Linki tam URL'ye çevirme
            if link and not link.startswith('http'):
                if link.startswith('/'):
                    link = config['url'] + link
                else:
                    link = config['url'] + '/' + link
            
            summary = item.select_one(config['selectors']['summary']) if config['selectors']['summary'] else None
            
            articles.append({
                'title': title.text.strip() if title else 'Başlık Yok',
                'link': link,
                'summary': summary.text.strip() if summary else 'Özet Yok'
            })
        
        return articles
    
    except Exception as e:
        print(f"{name} hatası: {str(e)}")
        return []

def generate_markdown(news_data):
    date = datetime.now().strftime("%Y-%m-%d")
    markdown = f"# Teknoloji Haber Özetleri ({date})\n\n"
    
    for site, articles in news_data.items():
        markdown += f"## {site}\n"
        for article in articles:
            markdown += f"### [{article['title']}]({article['link']})\n"
            markdown += f"> {article['summary']}\n\n"
    
    return markdown

def scrape_and_save():
    db_session = Session()
    all_news = {}
    
    for name, config in SITES.items():
        articles = scrape_site(name, config)
        all_news[name] = articles
        
        for article in articles:
            save_article(
                db_session,
                name,
                article['title'],
                article['link'],
                article['summary']
            )
    
    markdown_content = generate_markdown(all_news)
    with open("NEWS.md", "w", encoding="utf-8") as f:
        f.write(markdown_content)
    
    db_session.close()
    print("✅ Haberler veritabanına kaydedildi ve NEWS.md oluşturuldu!")

if __name__ == "__main__":
    scrape_and_save()