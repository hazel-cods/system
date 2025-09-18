from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class user(db.Model):
  id = db.Column(db.Integer,primary_key= True )
  username = db.Column(db.String(150),unique=True,nullable=False)
  email = db.Column(db.String(150),unique=True,nullable=False)
  password = db.Column(db.String(200),nullable=False)
  role = db.Column(db.String(50),default="student")