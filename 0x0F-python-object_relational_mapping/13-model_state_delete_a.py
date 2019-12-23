#!/usr/bin/python3
"""this script deletes all State objects whit a name containning the
letter a """

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
    del_ob = i_hel.query(State).filter(State.name.like('%a%'))

    for get in del_ob:
        i_hel.delete(get)

    i_hel.commit()
    i_hel.close()
