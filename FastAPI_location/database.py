from sqlalchemy import Engine, create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.ext.declarative import declarative_base



database_url = "postgresql://aamirlucky60:AhJX4ZpVc8mS@ep-weathered-base-a51yuvs0.us-east-2.aws.neon.tech/location?sslmode=require"
engine  = create_engine(database_url, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

session = SessionLocal()

class Base(DeclarativeBase) :
    pass
# create table
class Location(Base):
    __tablename__ = "location"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    location = Column(String)


Base.metadata.create_all(engine)
# adding columns
# Loc = Location(name="zia", location="Karachi")
# # Loc1 = Location(name="ali", location="Lahore")
# Loc2 = Location(name="saqib", location=" harbanspura,Lahore")
# Loc3 = Location(name="rizwan", location="bhatti chowk,Lahore")
# Loc4 = Location(name="aamir", location="Faisalabad")
# session.add(Loc)
# session.add(Loc1)
# session.add(Loc2)
# session.add(Loc3)
# session.add(Loc4)
# session.commit()