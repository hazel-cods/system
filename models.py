from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    tablename = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.Enum('student', 'teacher', 'admin'), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.current_timestamp())

    def repr(self):
        return f"<User {self.email} - {self.role}>"