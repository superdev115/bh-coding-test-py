# -*- coding: utf-8 -*-
from project import app
from flask import render_template, request, flash
from flask_wtf import FlaskForm
from wtforms.fields import StringField, SelectField, html5 as html5fields
from wtforms.validators import DataRequired, NumberRange, Regexp
from wtforms.widgets import html5 as html5widgets

from project.models.product import Product
from project.models.product_manager import ProductManager

productManager = ProductManager()

class AddProductForm(FlaskForm):
    customerId = StringField('Customer Id', validators=[DataRequired()])
    product_name = SelectField('Product Name', choices=[('domain', 'Domain'), ('hosting', 'Hosting'), ('email', 'Email'), ('pdomain', 'P-Domain'), ('edomain', 'E-Domain')], validators=[DataRequired()])
    domain = StringField('Domain', validators=[DataRequired(), Regexp('[a-z0-9-]+\.(?:com|org|edu)')])
    duration_months = html5fields.IntegerField('Duration Months', widget=html5widgets.NumberInput(min=1, max=36), validators=[DataRequired(), NumberRange(min=1, max=36)])

@app.route('/')
@app.route('/load_products')
def load_products():
    return render_template('main/load_products.html', products=productManager.products)

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    form = AddProductForm(request.form)
    if request.method == 'POST' and form.validate():
        p = Product(form.customerId.data,
                    form.product_name.data,
                    form.domain.data,
                    form.duration_months.data)

        if productManager.duplicated(p):
            flash("Duplicated data!")
        else:
            if p.check_domain():
                if productManager.exist_domain(p):
                    productManager.add(p)
                    return render_template('main/load_products.html', products=productManager.products)
                else:
                    flash("Domain must be registered!")
            else:
                flash("Invalid domain!")

    return render_template('main/add_product.html', form=form)

@app.route('/demo_data')
def demo_data():
    productManager.demo_data()
    return render_template('main/load_products.html', products=productManager.products)

@app.route('/list_products')
def list_products():
    return render_template('main/list_products.html', products=productManager.list_products())

@app.route('/email_schedule')
def email_schedule():
    return render_template('main/email_schedule.html', products=productManager.email_schedule())
