
from bs4 import BeautifulSoup
import requests
from models import ScraperResponse, ScraperState


async def scraping(url: str):
    scraperResponse = ScraperResponse()
    print(f"url {url}")
    headers = {"User-Agent":"Mozilla/5.0"}
    try:
        response = requests.get(url, headers = headers)
        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.string if soup.title else "No title"
        article_content = soup.find(class_="article-content")
        date = "N/E"
        content = "N/E"
        if article_content:
            time_tag = article_content.find("time")
            if time_tag and "datetime" in time_tag.attrs:
                date = time_tag["datetime"]
            content = [ p.get_text() for p in article_content.find_all("p")]
        scraperResponse.date = date
        
        scraperResponse.content = " ".join(content) if isinstance(content, list) else content
        scraperResponse.title = title
        scraperResponse.url = url
        return scraperResponse
    except requests.RequestException as e:
        scraperResponse.state = ScraperState.FAILED
        return scraperResponse
    
    