from flask import Blueprint, render_template, request, redirect

from pybo import db
from pybo.models import Product

bp = Blueprint('store', __name__, url_prefix='/store')

@bp.route("/main")
def store_main():
    products = Product.query.all()
    return render_template("store.html", products=products)

@bp.route("/product/<int:id>")
def product(id):
    product = Product.query.get_or_404(id)
    return render_template("product.html", product=product)

@bp.route("/product/add", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        product = Product(
            Productname=request.form["name"],
            Producttype=request.form["type"],
            Productprice=request.form["price"],
            stock=request.form["stock"],
            Productdescription=request.form["description"],
            Productimage_url=request.form["image_url"],
            Productlimit = request.form["limit"],
            Productdate = request.form["date"]
        )

        db.session.add(product)
        db.session.commit()
        return redirect("/store/product/add")

    return render_template("add_product.html")

