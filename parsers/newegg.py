from bs4 import BeautifulSoup
from external.request import get
from Information import Information

def newegg_parser(query):
    if not query:
        return [Information("", "", "", "")]
    template = "https://www.newegg.com/p/pl?d={}"
    url = template.format(query.replace(" ", "+"))
    text = get(url)
    soup = BeautifulSoup(text, 'html.parser')
    items = soup.find_all("div", class_ = "item-container")
    results = list()
    for item in items:
        item_price = price(item)
        item_title = title(item)
        item_uri = uri(item)
        item_bids = "Buy Now" #bids(item)
        results.append(Information(item_title, item_price, item_bids, item_uri))
    return results


def price(item):
        name = item.find(class_ = "price-current")
        if name:
            if "strong" not in str(name):
                return ""
            price_str = "$"
            dollars = name.find("strong")
            if not dollars:
                return ""
            price_str += dollars.text
            cents = name.find("sup")
            if not cents:
                return ""
            price_str += cents.text
            return price_str
        return ""


def bids(item):
        bids = item.find("a", class_ = "price-current-num")
        if bids:
            return bids.text
        return ""


def title(item):
        title = item.find("a", class_ = "item-title")
        if title:
            return title.text
        return ""


def uri(item):
        uri = item.find("a", class_ = "item-title")
        if uri:
            return uri["href"]
        return ""
