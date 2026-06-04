import os
from dotenv import load_dotenv
from sqlalchemy import create_engine,text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

load_dotenv() 

DB_URL = os.getenv("DATABASE_URL")

if DB_URL is None:
    raise ValueError("DATABASE_URL is not set. Check your .env file")

engine = create_engine(DB_URL)

try: 
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1  "))
        print(f"connection succesful ! database response : {result.scalar()}")

except Exception as e:
    print("Connection failed!")
    print(f"Error details: {e}")





sessionLocal = sessionmaker(bind = engine)

Base = declarative_base()


