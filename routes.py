from flask import Blueprint, render_template
from database.models import Session, Article

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    session = Session()
    articles = session.query(Article).order_by(Article.created_at.desc()).limit(50).all()
    session.close()
    return render_template('index.html', articles=articles)