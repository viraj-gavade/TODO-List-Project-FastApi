from sqlalchemy.orm import  sessionmaker 
from sqlalchemy import create_engine

DB_URL =' postgresql://postgres:admin@localhost:5432/FastapiDB'

engine = create_engine(DB_URL)

session = sessionmaker(bind=engine,autoflush=False)


def ConnectDB():
    try:
        db = session()
        print('Connection Established Successfully!')
        yield db
    finally:
        db.close_all()
        print('Connection Closed')