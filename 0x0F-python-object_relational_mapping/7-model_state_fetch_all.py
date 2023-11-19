#!/usr/bin/python3
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
"""
script that lists all State objects from the database hbtn_0e_6_usa
"""


if __name__ == "__main__":
    mysql = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"
    db = create_engine(mysql)
    Base.metadata.create_all(db)
    Session = sessionmaker(bind=db)
    session = Session()
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
    session.close()
