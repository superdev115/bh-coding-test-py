# -*- coding: utf-8 -*-
from project import app
from flask import render_template

@app.route('/')
@app.route('/load_products')
def load_products():
    return render_template('main/load_products.html')

@app.route('/add_product')
def add_product():
    return render_template('main/add_product.html')

@app.route('/list_products')
def list_products():
    return render_template('main/list_products.html')

@app.route('/email_schedule')
def email_schedule():
    return render_template('main/email_schedule.html')
