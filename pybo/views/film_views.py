from flask import Blueprint, render_template

bp = Blueprint('film', __name__, url_prefix='/film')

@bp.route('/event', methods=['GET'])
def event():
    return render_template('event.html')

@bp.route('/store', methods=['GET'])
def store():
    return render_template('store.html')

@bp.route('/store/ticket', methods=['GET'])
def store_ticket():
    return render_template('store_ticket.html')

@bp.route('/movie/list', methods=['GET'])
def movie_list():
    return render_template('movie_list.html')

@bp.route('/movie/list/info/<int:movie_id>', methods=['GET'])
def movie_info(movie_id):
    return render_template('movie_info/movie_info_1.html', movie_id=movie_id)

@bp.route('/booking', methods=['GET','POST'])
def booking():
    return render_template('booking.html')