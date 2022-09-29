from select import select
from parsel import Selector
import requests
import time


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        if url == "":
            return []
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
            )
        if response.status_code != 200:
            return None
        return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    if html_content == []:
        return html_content
    selector = Selector(text=html_content)
    return selector.css(".entry-title a::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_button = selector.css(".next.page-numbers ::attr(href)").get()
    if next_button is None:
        return None
    return next_button


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
