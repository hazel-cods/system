# /routes/auth.py

from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User  # Make sure your models.py defines a User model

# Blueprint setup
auth_bp = Blueprint("auth", __name__)



@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        role = request.form.get("role", "student")  # default role as student if not provided

        # Check if user already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("Email already registered. Please log in.", "warning")
            return redirect(url_for("auth.login"))

        # Hash the password
        hashed_pw = generate_password_hash(password, method="pbkdf2:sha256")

        # Create new user
        new_user = User(email=email, password=hashed_pw, role=role)
        db.session.add(new_user)
        db.session.commit()

        flash("Account created successfully! You can now log in.", "success")
        return redirect(url_for("auth.login"))

    return render_template("auth/register.html")



@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            # Store session
            session["user_id"] = user.id
            session["email"] = user.email
            session["role"] = user.role

            flash(f"Welcome back, {user.email}!", "success")

            # Redirect based on role
            if user.role == "admin":
                return redirect(url_for("admin.dashboard"))
            elif user.role == "teacher":
                return redirect(url_for("teacher.dashboard"))
            else:
                return redirect(url_for("student.dashboard"))
        else:
            flash("Invalid email or password", "danger")

    return render_template("auth/login.html")


@auth_bp.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for("auth.login"))
