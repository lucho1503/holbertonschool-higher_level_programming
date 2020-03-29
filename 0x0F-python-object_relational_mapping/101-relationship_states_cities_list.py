#!/usr/bin/python3
""" this script prints all city objects in the database """

from sys import argv
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    hel = sessionmaker(bind=engine)
    i_hel = hel()
    sta_city = i_hel.query(State).outerjoin(City).order_by(State.id,
                                                           City.id).all()

    for state in sta_city:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))

    i_hel.close()
