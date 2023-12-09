from sqlalchemy import create_engine
from tables import Base

engine = create_engine('sqlite:///todo.db', echo=True)


# Create the table in the database
Base.metadata.create_all(engine)
