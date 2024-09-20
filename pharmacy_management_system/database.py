
# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

def setup_database():
    engine = create_engine('sqlite:///pharmacy.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()
