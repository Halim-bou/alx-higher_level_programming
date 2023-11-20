#!/usr/bin/python3
"""
lists all state
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State



if __name__ == "__main__":
    myeng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(myeng)
    Session = sessionmaker(bind=myeng)
    session = Session()
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
