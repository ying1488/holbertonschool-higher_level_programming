#!/usr/bin/python3
"""Prints the first State objects from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.
        format(username, password, db)
        )

    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    states = session.query(State).order_by(State.id).first()
    if states:
        print("{}: {}".format(states.id, states.name))
    else:
        print("Nothing")

    session.close()
