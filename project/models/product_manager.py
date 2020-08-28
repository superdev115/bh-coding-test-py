# -*- coding: utf-8 -*-
from datetime import date
from project.models.product import Product

class ProductManager:

    products = []

    def add(self, customerId, productName, domain, durationMmonths):
        self.products.append(Product(customerId, productName, domain, durationMmonths))

    def add(self, product):
        self.products.append(product)

    def demo_data(self):
        self.products.clear()
        self.products.append(Product("Cust123", "domain", "xyzzy.com", 12, date(2020, 1, 1)))
        self.products.append(Product("Cust123", "hosting", "xyzzy.com", 6, date(2020, 1, 1)))
        self.products.append(Product("Cust234", "domain", "plugh.org", 24, date(2020, 2, 1)))
        self.products.append(Product("Cust123", "domain", "mydomain.com", 12, date(2020, 3, 1)))
        self.products.append(Product("Cust123", "email", "mydomain.com", 12, date(2020, 3, 1)))
        self.products.append(Product("Cust345", "pdomain", "protected.org", 36, date(2020, 3, 1)))
        self.products.append(Product("Cust456", "edomain", "school.edu", 12, date(2020, 4, 1)))
        self.products.append(Product("Cust345", "hosting", "protected.org", 11, date(2020, 4, 1)))

        return self.products
