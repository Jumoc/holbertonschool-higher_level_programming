#!/usr/bin/python3
"""Module state fetch first"""

from sqlalchemy import create_engine
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    # Create engine that connects to the core (MySQL)
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.
        format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
        )
    # Creates metadata and table schemes
    Base.metadata.create_all(engine)
    # Get the class of session and bind it with the engine
    Session = sessionmaker(bind=engine)
    # Instantiate the session
    session = Session()
    # The session object manages all the transactions
    result = session.query(State).first()

    if result is None:
        print('Nothing')
    else:
        print("{}: {}".format(result.id, result.name))
