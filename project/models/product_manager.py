# -*- coding: utf-8 -*-
from datetime import date
from project.models.product import Product

class ProductManager:

    products = []

    def add(self, customerId, productName, domain, durationMmonths):
        self.products.append(Product(customerId, productName, domain, durationMmonths))

    def add(self, product):
        self.products.append(product)

    def duplicated(self, prod):
        for product in self.products:
            if prod.productName == product.productName and prod.domain == product.domain:
                return True
        
        return False

    def exist_domain(self, prod):
        if prod.productName[-6:] == "domain":
            return True
        
        for product in self.products:
            if product.productName == "domain" and prod.domain == product.domain:
                return True
        
        return False

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

    def list_products(self):
        _products = list(self.products)
        _products.sort(key=lambda p: p.customerId, reverse=False)

        return _products

    def email_schedule(self):
        email_lists = []
        for product in self.products:
            email_lists += product.calc_email_dates()

        email_lists.sort(key=lambda e: e.startDate, reverse=False)
        
        return email_lists