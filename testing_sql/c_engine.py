from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker,declarative_base

sql_database_path="mysql+pymysql://root:123456@localhost/fastapidb"

engine=create_engine(sql_database_path)

sessionlocal=sessionmaker(bind=engine,autocommit=False,autoflush=False)

Base=declarative_base()

