from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

SECRET = b'patitosecurity'

engine = create_engine("mysql+pymysql://admin:fernandez21R@datatesis.cjwlwkvq6cdy.us-east-1.rds.amazonaws.com:3306/datatesisBD",isolation_level="READ UNCOMMITTED")

meta = MetaData()

conn = engine.connect()

Base = declarative_base()

Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def get_session():
    s = Session()
    try:
        yield s
    finally:
        s.close()

def get_db_connection():
    return engine.connect()