from Site import Site
from Product import Product
from Information import Information
from parsers.ebay import ebay_parser
from parsers.newegg import newegg_parser
from jinja2 import Template
from markupsafe import escape
from flask import Flask, request
import sys


app = Flask(__name__)
query = None


def do_ebay(query = None):
    ebay = Site("eBay", ebay_parser)

    ebay_gfx_card = Product(query, ebay)
    return ebay_gfx_card.search()


def do_newegg(query = None):
    newegg = Site("Newegg", newegg_parser)

    newegg_gfx_card = Product(query, newegg)
    return newegg_gfx_card.search()


@app.route("/", methods=["GET"])
def homepage():
    with open("templates/home.html") as temp_file:
        template = Template(temp_file.read())
    html = template.render()
    return html


@app.route("/", methods=["POST"])
def search():
    query = ""
    if request.method == "POST":
        query = request.form.get("query")
    data = list()
    data += do_ebay(query)
    data += do_newegg(query)
    with open("templates/search.html") as temp_file:
        template = Template(temp_file.read())
    html = template.render(data=data, query=query)
    return html
