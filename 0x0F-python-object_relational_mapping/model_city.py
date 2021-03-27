#!/usr/bin/python3
"""Model model city"""

from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import false
from model_state import Base
from sqlalchemy import Column, String, Integer, ForeignKey


class City(Base):
    """Class City that will map to the MySQL table cities
        attributes:
            __tablename_: the name of the mapped table
            id: id of the city
            name: name of the city
            state_id: id of a state (foreign key)
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
