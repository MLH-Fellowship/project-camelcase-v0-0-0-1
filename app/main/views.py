from . import main
from flask import render_template
import os

@main.route('/')
def index():
    return render_template('index.html', title="Meet us", url=os.getenv("URL"))
