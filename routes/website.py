from flask import Blueprint, render_template

website_bp = Blueprint("website",__name__,template_folder="../templates/website")


@app.route("/")
def home():
  return render_template("website/home.html")

@app.route("/login")
def login():
  return render_template("login.html")

@app.route("/courses")
def courses():
  return render_template("website/courses.html")

@app.route("/enrollment")
def enrollment():
  return render_template("enrollment.html")

@app.route("/base")
def base():
  return render_template("website/base.html")
