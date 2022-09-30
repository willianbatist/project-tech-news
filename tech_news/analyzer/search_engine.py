from datetime import datetime
from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    get_news = search_news({"title": {"$regex": title, "$options": "i"}})
    result = []
    for row in get_news:
        result.append((row["title"], row["url"]))
    return result


# Requisito 7
def search_by_date(date):
    try:
        date1 = "%Y-%m-%d"
        date2 = "%d/%m/%y"
        date_one = datetime.strptime(date, date1)
        date_two = datetime.strptime(date_one, date2)
        get_news = search_news(
            {"timestamp": {"$regex": date_two, "$option": "i"}}
        )
        result = [(row["title"], row["url"]) for row in get_news]
        return result
    except Exception:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
