from flask import Blueprint, render_template

bp = Blueprint('movie', __name__, url_prefix='/movie')

@bp.route('/movie/list', methods=['GET'])
def movie_list():
    return render_template('movie_list.html')

