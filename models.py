from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class Article(Base):
    __tablename__ = 'articles'
    
    id = Column(Integer, primary_key=True)
    site_name = Column(String(50), nullable=False)
    title = Column(String(255), nullable=False)
    link = Column(String(255), unique=True, nullable=False)
    summary = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

# Veritabanı bağlantısı
engine = create_engine('sqlite:///news.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)