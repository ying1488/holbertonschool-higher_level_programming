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
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states_a = session.query(State)\
        .filter(State.name.like('%a%'))\
        .order_by(State.id).all()
    for state in states_a:
        print(f"{state.id}: {state.name}")

    session.close()
