from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Visit(db.Model):
    __tablename__ = "visits"

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    ip = db.Column(db.String(45), nullable=False)

    def __repr__(self):
        return f"<Visit {self.id} {self.ip} {self.timestamp}>"