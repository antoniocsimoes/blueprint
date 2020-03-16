#blueprint serve para modularizar a aplicação

from flask import Flask

app = Flask(__name__)

from app.main import main as main_blueprint
app.register_blueprint(main_blueprint)

from app.products import products as products_blueprint
app.register_blueprint(products_blueprint)

# @app.route("/")
# def home():
#     return "Home Page"

# @app.route("/login")
# def login():
#     return "Login Page"

# @app.route("/register")
# def register():
#     return "Register Page"

# @app.route("/products")
# def products():
#     return "Products Page"

# @app.route("/categories")
# def categories():
#     return "Categories Page"