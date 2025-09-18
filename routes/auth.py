from flask import Blueprint, render_template, redirect, url_for, request, flash, session

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


#register route
@auth_bp.route("/register", methods=["GET", "POST"])
def register():
  if request.method == "POST":
    email = request.form.get("email")
    password = request.form.get("password")
    role = request.form.get("role")

    flash("Account created successfully!", "success")
    return redirect(url_for("auth.login"))
  
  return render_template("auth/register.html")



#login route
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
  if request.method == "POST":
    email = request.form.get("email")
    password = request.form.get("password")

    role = "student"

    #store session
    session['user'] = email
    session['role'] = role

    flash(f"Welcome back, {email}!", "success")


    #redirect base on role
    if role == "admin":
      return redirect(url_for("admin.dashboard"))
    elif role == "teacher":
      return redirect(url_for("teacher.dashboard"))
    else: 
      return redirect(url_for("student.dashboard"))
  return render_template("auth/login.html")

#logout route
@auth_bp.route("/logout")
def logout():
  flash("You have been logged out.", "info")
  return redirect(url_for("auth.login"))
    
