class Information:

    def __init__(self, name, price, bids, uri):
        self.name = name
        self.price = price
        self.bids = bids
        self.uri = uri


    def html(self):
        return "<h3><a href=\"{}\">{}</a></h3><p>{}</p><p>{}</p>".format(self.uri, self.name, self.price, self.bids)
