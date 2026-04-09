from flask import Blueprint, url_for, redirect, render_template

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    return render_template('main.html')
