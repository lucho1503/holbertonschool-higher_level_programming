#!/usr/bin/python3
""" this script prints the first state object from the database """

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
    get = i_hel.query(State).first()

    if get is not None:
        print("{}: {}".format(get.id, get.name))
    else:
        print("Nothing")

    i_hel.close()
