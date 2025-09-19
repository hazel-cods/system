from flask import Blueprint, render_template

teacher_bp = Blueprint("teacher", __name__, url_prefix="/teacher")

@teacher_bp.route("/dashboard")
def dashboard():
  return render_template("dashboard/dash_teacher.html")

@teacher_bp.route("/schedules")
def schedules():
  return render_template("students/schedules.html")

@teacher_bp.route("/grades")
def grades():
  return render_template("students/grades.html")