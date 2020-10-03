
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://mysqlalchemy:Darkmoon!@localhost/MySQLAlchemy', pool_recycle=3600)
