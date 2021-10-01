import logging


class Site:

    def __init__(self, name, parser):
        self.name = name
        self.parser = parser


    def parse(self, query):
        logging.info("Running {} parser.".format(self.name))
        result = self.parser(query)
        logging.info("Finished {} parser.".format(self.name))
        return result
