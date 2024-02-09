from typing import Optional
from sqlmodel import  select, Field, SQLModel, Session, create_engine

class Location(SQLModel, table = True):
    id : Optional[int] = Field(default =None, primary_key = True)
    name  : str
    location : str

engine = create_engine("postgresql://aamirlucky60:AhJX4ZpVc8mS@ep-weathered-base-a51yuvs0.us-east-2.aws.neon.tech/loc_sqlmodel?sslmode=require")


# loc1 = Location(name = "aamir", location = "Faisalabad ")
# loc2 = Location(name = "rizwan", location = "Lahore ")
# loc3 = Location(name = "asad", location = "karachi ")

SQLModel.metadata.create_all(engine)

# with Session(engine) as session:
    # session.add(loc1)
    # session.add(loc2)
    # session.add(loc3)
    # session.commit()

