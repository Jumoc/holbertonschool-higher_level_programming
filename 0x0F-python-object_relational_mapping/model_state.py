#!/usr/bin/python3
"""Module for model state"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()


class State(Base):
    """Class State that will map to the MySQL table states
        attributes:
            __tablename_: the name of the mapped table
            id: id of the state
            name: name of the state
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
