from . import products

@products.route("/products")
def products_page():
    return "Products Page Blueprint"