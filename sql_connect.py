from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Replace with your database URL
DATABASE_URL = 'sqlite:///example.db'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

if sql_condition:
    query = f"SELECT * FROM users WHERE {sql_condition}"
    result = session.execute(query)
    for row in result:
        print(row)
else:
    print("Unable to generate a valid SQL condition.")
