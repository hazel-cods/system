from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db

student_bp = Blueprint("student", __name__, url_prefix="/student")

@student_bp.route("/dashboard")
def dashboard():
  return render_template("dashboard/dash_student.html")

@student_bp.route("/courses")
def courses():
  return render_template("students/courses.html")

@student_bp.route("/grades")
def grades():
  return render_template("students/grades.html")

@student_bp.route("/schedules")
def schedules():
  return render_template("students/schedules.html")
