from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    password = Column(String)
    avatarId = Column(Integer)

    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}s'>"

