from . import main
from flask import render_template
import os

@main.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@main.route('/gabby')
def about_gabby():
    return render_template('about_gabby.html', title="MLH Fellow", url=os.getenv("URL"))

@main.route('/dario')
def about_dario():
    return render_template('about_dario.html', title="MLH Fellow", url=os.getenv("URL"))