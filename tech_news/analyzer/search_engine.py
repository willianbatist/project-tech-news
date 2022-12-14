from datetime import datetime
from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    get_news = search_news({"title": {"$regex": title, "$options": "i"}})
    result = []
    for row in get_news:
        result.append((row["title"], row["url"]))
    return result


# ajuda by João Keuwe T17
# Requisito 7
def search_by_date(date):
    try:
        date_one = datetime.strptime(date, "%Y-%m-%d")
        date_two = datetime.strftime(date_one, "%d/%m/%Y")
        get_news = search_news(
            {"timestamp": {"$regex": date_two, "$options": "i"}}
        )
        result = [(row["title"], row["url"]) for row in get_news]
        return result
    except Exception:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    get_news = search_news({"tags": {"$regex": tag, "$options": "i"}})
    result = []
    for row in get_news:
        result.append((row["title"], row["url"]))
    return result


# Requisito 9
def search_by_category(category):
    get_news = search_news({"category": {"$regex": category, "$options": "i"}})
    result = []
    for row in get_news:
        result.append((row["title"], row["url"]))
    return result
