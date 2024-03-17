#!/usr/bin/python3
"""a script that deletes all State objects
with a name containing the letter a"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_city import City

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state, city_id, city_name in (session.query(State.name, City.id, City.name)
                                      .join(City, State.id == City.state_id)):
        print("{}: ({}) {}".format(state, city_id, city_name))
