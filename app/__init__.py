import os
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from peewee import *
from playhouse.shortcuts import model_to_dict
from crypt import methods
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

bootstrap = Bootstrap()
bootstrap.init_app(app)

#print("DATOS ++++++++",os.getenv("URL"))

mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=3306
)
print(mydb)

@app.route('/')
def index():
    return render_template('index.html', title="Meet us", url=os.getenv("URL"))

@app.route('/gabby')
def about_gabby():
    return render_template('about_gabby.html', title="MLH Fellow", url=os.getenv("URL"))


@app.route('/places/<string:for_person>')
def visited_map(for_person: str = None):
    if for_person is not None and for_person.lower() == 'dario':
        return send_file('templates/maps/dario-places-visited.html')

    if for_person is not None and for_person.lower() == 'gabby':
        return jsonify({"message": 'map not yet available'}), 200

    return jsonify({"message": "resource not found"}), 404


@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    timeline_post = TimelinePost.create(name=name, email=email, content=content)

    return timeline_post.to_json()

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    posts = TimelinePost.select().order_by(TimelinePost.created_at.desc())
    return {
        'timeline_posts': [post.to_json() for post in posts]
    }

@app.route('/timeline')
def timeline():
    return render_template('timeline.html', title="Timeline")