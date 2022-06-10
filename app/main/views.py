from . import main
from flask import abort, jsonify, render_template, send_file
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

@main.route('/places/<string:for_person>')
def visited_map(for_person: str = None):
    if for_person is not None and for_person.lower() == 'dario':
        return send_file('templates/maps/dario-places-visited.html')
    
    if for_person is not None and for_person.lower() == 'gabby':
        return jsonify({"message": 'map not yet available'}), 200

    return jsonify({"message": "resource not found"}), 404
    

