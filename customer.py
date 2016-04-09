ORDERS = ['order1', 'order2']

class Customer:

    def __init__(self, name):
        self.name = name
        self.orders = self.get_orders()

    def get_orders(self):
        # resource-intensive code, say
        orders =ORDERS
        return orders

class BetterCustomer(Customer):

    _orders = None

    def __init__(self, name):
        self.name = name

    @property
    def orders(self):
        if self._orders is None:  # first time referenced
            self._orders = self.get_orders()
        return self._orders



