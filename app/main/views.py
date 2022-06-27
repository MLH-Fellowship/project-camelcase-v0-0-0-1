from . import main
from flask import abort, jsonify, render_template, send_file, redirect, url_for
import os
from app.models import TimelinePost
from .forms import TimelinePostForm

@main.route('/')
def index():
    return render_template('index.html', title="Meet us", url=os.getenv("URL"))

@main.route('/gabby/')
def about_gabby():
    return render_template('about_gabby.html', title="MLH Fellow", url=os.getenv("URL"))

@main.route('/dario/')
def about_dario():
    return render_template('about_dario.html', title="MLH Fellow", url=os.getenv("URL"))

@main.route('/timeline/', methods=['GET', "POST"])
def timeline():
    form = TimelinePostForm()
    if form.validate_on_submit():
        post = TimelinePost(name=form.name.data, email=form.email.data, content=form.content.data)
        try: 
            post.save()
        except:
            return abort(422)
        return redirect(url_for('main.timeline'));
    posts = TimelinePost.select()
    return render_template('timeline.html', title='Timeline', form=form, timeline_events=[post for post in posts])


@main.route('/places/<string:for_person>')
def visited_map(for_person: str = None):
    if for_person is not None and for_person.lower() == 'dario':
        return send_file('templates/maps/dario-places-visited.html')
    return jsonify({"message": "resource not found"}), 404
    
