"""
Main module of the server file
"""
import mimetypes
from requests import Response
from flask import render_template
import config

# Get the application instance
connex_app = config.connex_app

# Read the swagger.yml file to configure the endpoints
connex_app.add_api("swagger.yml")

# create a URL route in our application for "/"
@connex_app.route("/")
def home():
    return render_template("home.html")

@connex_app.route("/tutorial")
def tutorial():
    with open('./assets/panduan.txt', 'r', encoding = 'utf-8') as f:
        return render_template("tutorial.html", text = f.read())

if __name__ == "__main__":
    connex_app.run(debug=True)