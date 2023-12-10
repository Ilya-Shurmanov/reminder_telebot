from sqlalchemy import Column, Integer, String, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base

from db_tools.configuration import db_file

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String)
    is_admin = Column(Boolean, default=False)
    telegram_id = Column(String)


engine = create_engine(db_file, echo=True)


# Create the table in the database
Base.metadata.create_all(engine)
