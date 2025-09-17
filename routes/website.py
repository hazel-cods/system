from flask import Blueprint, render_template

website_bp = Blueprint("website",__name__,template_folder="../templates/website")

@website_bp("/")
def base():
  return render_template("website/base.html")

@website_bp("/about")
def about():
  return render_template("website/about.html")

@website_bp("/academics")
def academics():
  return render_template("website/academics.html")

@website_bp("/admission")
def admission():
  return render_template("website/admission.html")

@website_bp("/contact")
def contact():
  return render_template("website/contact.html")

@website_bp("/home")
def home():
  return render_template("website/home.html")