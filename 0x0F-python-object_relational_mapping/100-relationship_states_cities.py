#!/usr/bin/python3
""" this script creates the State object California with the citi
San francisco from the database """

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    hel = sessionmaker(bind=engine)
    i_hel = hel()

    new_state = State(name='California')
    new_city = City(name='San Francisco')
    new_state.cities.append(new_city)

    i_hel.add(new_state)
    i_hel.add(new_city)
    i_hel.commit()
