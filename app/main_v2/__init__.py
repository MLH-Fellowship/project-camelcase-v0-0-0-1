from flask import Blueprint

main_v2 = Blueprint('main_v2', __name__)

from . import views