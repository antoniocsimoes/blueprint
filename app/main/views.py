from . import main

@main.route("/")
def home():
    return "Home Page Blueprint"