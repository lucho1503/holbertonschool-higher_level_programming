#!/usr/bin/python3
""" this sxript contains the class definition of a city """

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.orm import relationship

from sqlalchemy.ext.declarative import declarative_base

mtdata = MetaData()
Base = declarative_base(metadata=mtdata)


class State(Base):
    """ class that defines each city """

    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states")
