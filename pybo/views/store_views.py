from flask import Blueprint, render_template, request, redirect, abort, url_for, session

from pybo import db
from pybo.models import Product, Order, User

bp = Blueprint('store', __name__, url_prefix='/store')

@bp.route("/main")
def store_main():
    products = Product.query.all()
    return render_template("store.html", products=products)

@bp.route("/product/<int:id>")
def product(id):
    product = Product.query.get_or_404(id)
    return render_template("product.html", product=product)

# 주문 생성
@bp.route('/order/create/<int:product_id>')
def create_order(product_id):
    user = User.query.get(session.get("user_id"))
    product = Product.query.get(product_id)

    quantity = int(request.args.get('quantity', 1))  # 기본 1

    total_price = product.Productprice * quantity

    order = Order(
    user_id=user.id,
    user_name=user.username,
    user_userid=user.userid,
    product_id=product.id,
    product_name=product.Productname,
    quantity=quantity,
    total_price=total_price
)

    db.session.add(order)
    db.session.commit()

    return redirect(url_for('store.store_pay', order_id=order.id))

@bp.route('/pay')
def store_pay():
    order_id = request.args.get('order_id', type=int)

    order = Order.query.get_or_404(order_id)

    return render_template('store_pay.html', order=order)

@bp.route('/pay/success')
def pay_success():
    order_id = request.args.get("order_id", type=int)

    order = Order.query.get_or_404(order_id)
    order.status = "SUCCESS"

    db.session.commit()

    return "결제 완료!"
