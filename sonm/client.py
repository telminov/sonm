from . import deal
from . import order


class Client:
    def __init__(self):
        self.deal = deal.Deal()
        self.order = order.Order()
