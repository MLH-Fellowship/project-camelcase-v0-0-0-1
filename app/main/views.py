from . import main
from flask import abort, jsonify, render_template, send_file, request
import os
from app.models import TimelinePost


@main.route('/')
def index():
    return render_template('index.html', title="Meet us", url=os.getenv("URL"))

@main.route('/gabby')
def about_gabby():
    return render_template('about_gabby.html', title="MLH Fellow", url=os.getenv("URL"))


@main.route('/places/<string:for_person>')
def visited_map(for_person: str = None):
    if for_person is not None and for_person.lower() == 'dario':
        return send_file('templates/maps/dario-places-visited.html')
    
    if for_person is not None and for_person.lower() == 'gabby':
        return jsonify({"message": 'map not yet available'}), 200

    return jsonify({"message": "resource not found"}), 404


@main.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    timeline_post = TimelinePost.create(name=name, email=email, content=content)

    return timeline_post.to_json()

@main.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    posts = TimelinePost.select().order_by(TimelinePost.created_at.desc())
    return {
        'timeline_posts': [post.to_json() for post in posts]
    }

@main.route('/timeline')
def timeline():
    return render_template('timeline.html', title="Timeline")