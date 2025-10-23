from sqlalchemy.orm import  sessionmaker 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

DB_URL = 'postgresql://postgres:admin@localhost:5432/FastapiDB'

engine = create_engine(DB_URL)

session = sessionmaker(bind=engine,autoflush=False)


def ConnectDB():
    db = session()
    try:
        print('Connection Established Successfully!')
        yield db
    finally:
        db.close()
        print('Connection Closed')