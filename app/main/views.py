from . import main
from flask import render_template
import os

@main.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))
