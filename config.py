
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
  SECRET_KEY = "hazel"
  SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:Hazel123%401009@localhost/school_db"
  SQLALCHEMY_TRACK_MODIFICATIONS = False
