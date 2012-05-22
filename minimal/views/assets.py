from flask import Blueprint

assets = Blueprint('assets', __name__, static_folder='../static')
