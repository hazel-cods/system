from flask import Flask
from models import db
from routes.website import website_bp
from routes.auth import auth_bp
from routes.admin import admin_bp
from routes.student import student_bp
from routes.teacher import teacher_bp


def create_app():
  app = Flask(__name__, instance_relative_config=True)
  app.config.from_object("config.Config")
  db.init_app(app)
  
#Register Blueprints
  app.register_blueprint(website_bp,url_prefix="/")
  app.register_blueprint(auth_bp,url_prefix="/auth")
  app.register_blueprint(admin_bp,url_prefix="/admin")
  app.register_blueprint(teacher_bp,url_prefix="/teacher")
  app.register_blueprint(student_bp,url_prefix="/student")

  return app