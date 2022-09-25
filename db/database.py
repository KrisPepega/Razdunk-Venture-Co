from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

passwd = os.getenv("db_passwd")
user = os.getenv("db_user")
host = os.getenv("db_host")
port = os.getenv("db_port")
db = os.getenv("db")
dialect = os.getenv("db_dialect")
connector = os.getenv("db_connector")

url = f'mysql+mysqlconnector://{user}:{passwd}@{host}:{port}/{db}'
#print(url)

engine = create_engine(url, echo = True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

BASE = declarative_base()
