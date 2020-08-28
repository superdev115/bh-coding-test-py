# -*- coding: utf-8 -*-
from project import app
from flask import render_template

@app.route('/')
def start():
    return render_template('main/index.html')
