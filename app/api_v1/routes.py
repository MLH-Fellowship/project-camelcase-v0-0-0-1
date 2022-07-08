from flask import jsonify
from pymysql import Time
from . import api_v1
from app.models import TimelinePost
from flask import request

@api_v1.route('/timeline_post', methods=['POST'])
def post_time_line_post():
  print(request.form)
  post = TimelinePost.create(**request.form)
  
  try:
    post.save()
    return jsonify(post.to_json());
  except:
    return jsonify({"message": "unable to create post"}), 500


@api_v1.route('/timeline_post', methods=['GET'])
def get_time_line_post():
  query =  TimelinePost.select();
  return jsonify(
    {
      "timeline_posts": [record.to_json() for record in query]
    }
  )

@api_v1.route('/timeline_post/<int:id>', methods=['DELETE'])
def delete_time_line_post(id):
  try:
    post = TimelinePost.get(TimelinePost.id == id)
    rows = post.delete_instance()
    return jsonify({'message': f'post has been deleted', 'meta': f'rows affected: {rows}'})
  except:
    return jsonify({'message': 'unable to delete post'}), 422