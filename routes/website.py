from flask import Blueprint, render_template

website_bp = Blueprint("website", __name__ ,template_folder="templates/website")

@website_bp.route("/")
def base():
  return render_template("website/base.html")

@website_bp.route("/about")
def about():
  return render_template("website/about.html")

@website_bp.route("/academics")
def academics():
  return render_template("website/academics.html")

@website_bp.route("/admission")
def admission():
  return render_template("website/admission.html")

@website_bp.route("/contact")
def contact():
  return render_template("website/contact.html")

@website_bp.route("/home")
def home():
  return render_template("website/home.html")