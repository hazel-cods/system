from flask import Blueprint, render_template, redirect, url_for, request

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

#admin dashboard
@admin_bp.route("/dashboard")
def dashboard():
  return render_template("dashboard/dash_admin.html")

@admin_bp.route("/students")
def manage_students():
  return render_template("students/students.html")

@admin_bp.route("/courses")
def manage_courses():
  return render_template("students/courses.html")

@admin_bp.route("/teachers")
def manage_teachers():
  return render_template("Teacher management page (to be implemented)")
