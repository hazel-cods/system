from flask import Flask , render_template, redirect, url_for


app = Flask(__name__)



@app.route("/")
def index():
  return render_template("index.html")

@app.route("/login")
def login():
  return render_template("login.html")

@app.route("/courses")
def courses():
  return render_template("courses.html")

@app.route("/enrollment")
def enrollment():
  return render_template("enrollment.html")


if __name__ == "__main__":
  app.run(debug=True)