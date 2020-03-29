#!/usr/bin/python3
""" this script ptinrts the state object whit the name passed as argument """

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
    get = i_hel.query(State).filter(State.name == argv[4]).all()

    if get:
        for get_id in get:
            print("{}".format(get_id.id))
    else:
        print("Not found")

    i_hel.close()
