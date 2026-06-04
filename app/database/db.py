from sqlalchemy import create_engine,text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DB_URL = "postgresql://postgres:mohamad123%40@localhost:5432/data_platforme"


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


