#!/usr/bin/python3
""" this script list all state object that contain the letter a """

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    hel = sessionmaker(bind=engine)
    i_hel = hel()

    for state in i_hel.query(State).filter(State.name.like('%a%')):
        print("{}: {}".format(state.id, state.name))

    i_hel.close()
