from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()


class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    groupName = Column(String, unique=True)
    password = Column(String)

    def __repr__(self):
        return f"<Group(name='{self.groupName}'"
