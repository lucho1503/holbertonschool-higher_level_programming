#!/usr/bin/python3
"""this script adds the State object "Lousiana" to the database """

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

    new_obj = State(name="Louisiana")
    i_hel.add(new_obj)
    i_hel.commit()
    print(new_obj.id)

    i_hel.close()
