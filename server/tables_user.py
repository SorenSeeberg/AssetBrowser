from mr_database import MrDatabase
from mr_database import Table
from mr_database import Column
from mr_database import DataTypes


class User(Table):

    id = Column(DataTypes.integer, pk=True)
    enabled = Column(DataTypes.smallint, default=0)
    userName = Column(DataTypes.varchar(60), unique=True)
    email = Column(DataTypes.varchar(60), unique=True)
    emailVerified = Column(DataTypes.smallint, default=0)
    password = Column(DataTypes.varchar(60))
    profilePicture = Column(DataTypes.varchar(60))
