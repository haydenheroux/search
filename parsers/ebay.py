from bs4 import BeautifulSoup
from lib.request import get
from Information import Information


def ebay_parser(query):
    if not query:
        return [Information("", "", "", "")]
    template = "https://www.ebay.com/sch/i.html?_nkw={}"
    url = template.format(query.replace(" ", "+"))
    text = get(url)
    soup = BeautifulSoup(text, 'html.parser')
    items = soup.find_all(class_ = "s-item__info")
    results = list()
    for item in items[1:]:
        item_name = name(item)
        item_price = price(item)
        item_option = option(item)
        item_uri = uri(item)
        results.append(Information(item_name, item_price, item_option, item_uri))
    return results


def name(item):
    name = item.find("h3", class_ = "s-item__title")
    if name:
        popups = name.find_all("span")
        for popup in popups:
            popup.decompose()
        return name.text
    return ""


def price(item):
    price = item.find("span", class_ = "s-item__price")
    if price:
        if not "See" in price.text:
            return price.text
    return ""


def option(item):
    options = item.find_all("span", class_ = "s-item__purchase-options-with-icon")
    buy_options = [option.text for option in options]
    if buy_options:
        return buy_options[0]
    bids = item.find("span", class_ = "s-item__bidCount")
    if bids:
        return bids.text
    return ""


def uri(item):
    uri = item.find("a", class_ = "s-item__link")
    if uri:
        return uri["href"]
    return ""
