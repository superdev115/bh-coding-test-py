# -*- coding: utf-8 -*-
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta

class Product:

    def __init__(self, customerId, productName, domain, durationMmonths, startDate = date.today()):
        self.customerId = customerId
        self.productName = productName
        self.domain = domain
        self.durationMmonths = durationMmonths
        self.startDate = startDate

    def check_domain_dp(self):
        return self.domain[-4:] == ".com" or self.domain[-4:] == ".org"

    def check_domain_e(self):
        return self.domain[-4:] == ".edu"

    def check_domain(self):
        if self.productName == "domain" or self.productName == "pdomain":
            return self.check_domain_dp()
        elif self.productName == "edomain":
            return self.check_domain_e()
        else:
            return True

    def calc_email_dates(self):
        email_dates = []

        if self.productName == "domain" or self.productName == "pdomain" or self.productName == "edomain":
            d = self.startDate + relativedelta(months=+self.durationMmonths) - timedelta(days=3)
            e = Product(self.customerId, self.productName, self.domain, self.durationMmonths, d)
            email_dates.append(e)
        elif self.productName == "hosting":
            d1 = self.startDate + timedelta(days=1)
            e1 = Product(self.customerId, self.productName, self.domain, self.durationMmonths, d1)
            d2 = self.startDate + relativedelta(months=+self.durationMmonths) - timedelta(days=4)
            e2 = Product(self.customerId, self.productName, self.domain, self.durationMmonths, d2)
            email_dates.append(e1)
            email_dates.append(e2)
        elif self.productName == "email":
            d = self.startDate + relativedelta(months=+self.durationMmonths) - timedelta(days=2)
            e = Product(self.customerId, self.productName, self.domain, self.durationMmonths, d)
            email_dates.append(e)
        
        return email_dates
    