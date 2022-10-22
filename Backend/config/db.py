from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

SECRET = b'patitosecurity'

engine = create_engine("mysql+pymysql://root:root@127.0.0.1:3306/desa",isolation_level="READ UNCOMMITTED")

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