#!/usr/bin/python3
""" this script prints all city objects in the database """

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    hel = sessionmaker(bind=engine)
    i_hel = hel()
    sta_city = i_hel.query(State, City).filter(State.id == City.state_id).all()

    for state, city in sta_city:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    i_hel.close()
