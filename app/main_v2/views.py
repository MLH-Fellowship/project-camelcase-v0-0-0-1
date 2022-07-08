from . import main_v2
from .forms import TimelinePostForm
from flask import render_template, abort, url_for, redirect
from app.models import TimelinePost

@main_v2.route('/')
def index():
  return render_template("/ui_v2/index_v2.html")

@main_v2.route('/timeline', methods=['GET', "POST"])
def timeline():
  form = TimelinePostForm()
  if form.validate_on_submit():
    post = TimelinePost(name=form.name.data, email=form.email.data, content=form.content.data)
    try: 
        post.save()
    except:
        return abort(422)
    return redirect(url_for('main_v2.timeline'));
  posts = TimelinePost.select().order_by(TimelinePost.created_at.desc())
  return render_template('/ui_v2/timeline_v2.html', form = form, timeline_events=[post for post in posts])

@main_v2.route('/projects')
def projects():
  return render_template('/ui_v2/projects_v2.html')

@main_v2.route('/ph/')
def placeholder():
  return render_template("/ui_v2/base_v2.html")

@main_v2.route('/ph/large')
def placeholder_large():
  return render_template("/ui_v2/base-large_v2.html")