from statistics import mean

class Coffee:

    original_value = None
    flag = False

    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if self.flag:
            self._name = self.original_value 
        else:
            self._name = name
            self.flag = True
            self.original_value = name
        
    def orders(self):
        return [result for result in Order.all if result.coffee == self]
    
    def customers(self):
        return list({result.customer for result in self.orders()})
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        return mean([result.price for result in self.orders()])

class Customer:

    original_value = None

    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            self._name = self.original_value
        elif not 1 <= len(name) <= 15:
            self._name = self.original_value
        else:
            self._name = name
            self.original_value = name
        
    def orders(self):
        return [result for result in Order.all if result.customer == self]
    
    def coffees(self):
        return list({result.coffee for result in self.orders()})
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
class Order:

    all = []
    original_value = None
    flag = False

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        type(self).all.append(self)

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if self.flag:
            self._price = self.original_value 
        elif not type(price) in (int, float):
            self._price = self.original_value 
        else:
            self._price = price
            self.flag = True
            self.original_value = price