#!/usr/bin/python3
""" this script changes the name of a State object from the database """

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
    update = i_hel.query(State).filter(State.id == 2).first()
    update.name = "New Mexico"
    i_hel.commit()

    i_hel.close()
