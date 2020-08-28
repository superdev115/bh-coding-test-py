# -*- coding: utf-8 -*-
from project import app
from flask import render_template, request
from flask_wtf import FlaskForm
from wtforms.fields import StringField, SelectField, html5 as html5fields
from wtforms.validators import DataRequired, NumberRange, Regexp
from wtforms.widgets import html5 as html5widgets

class AddProductForm(FlaskForm):
    customerId = StringField('Customer Id', validators=[DataRequired()])
    product_name = SelectField('Product Name', choices=[('domain', 'Domain'), ('hosting', 'Hosting'), ('email', 'Email'), ('pdomain', 'P-Domain'), ('edomain', 'E-Domain')], validators=[DataRequired()])
    domain = StringField('Domain', validators=[DataRequired(), Regexp('[a-z0-9-]+\.(?:com|org)')])
    duration_months = html5fields.IntegerField('Duration Months', widget=html5widgets.NumberInput(min=1, max=36), validators=[DataRequired(), NumberRange(min=1, max=36)])

@app.route('/')
@app.route('/load_products')
def load_products():
    return render_template('main/load_products.html')

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    form = AddProductForm(request.form)
    if request.method == 'POST' and form.validate():
        return render_template('main/load_products.html')
    return render_template('main/add_product.html', form=form)

@app.route('/list_products')
def list_products():
    return render_template('main/list_products.html')

@app.route('/email_schedule')
def email_schedule():
    return render_template('main/email_schedule.html')
