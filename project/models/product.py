# -*- coding: utf-8 -*-
from datetime import date

class Product:

    def __init__(self, customerId, productName, domain, durationMmonths, startDate = date.today()):
        self.customerId = customerId
        self.productName = productName
        self.domain = domain
        self.durationMmonths = durationMmonths
        self.startDate = startDate
    