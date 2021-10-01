class Product:

    def __init__(self, query, site):
        self.query = query
        self.site = site


    def search(self):
        return self.site.parse(self.query)
