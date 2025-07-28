from .models import Session, Article

def save_article(session, site_name, title, link, summary):
    # Aynı link varsa ekleme
    if not session.query(Article).filter_by(link=link).first():
        new_article = Article(
            site_name=site_name,
            title=title,
            link=link,
            summary=summary
        )
        session.add(new_article)
        session.commit()

def get_recent_articles(session, limit=20):
    return session.query(Article).order_by(Article.created_at.desc()).limit(limit).all()