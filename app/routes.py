from datetime import datetime
from flask import Blueprint, request
from .models import db, Visit

bp = Blueprint("main", __name__)

@bp.route("/hello", methods=["GET"])
def hello():
    ip = request.remote_addr

    visit = Visit(timestamp=datetime.utcnow(), ip=ip)
    db.session.add(visit)
    db.session.commit()

    return "Hello", 200