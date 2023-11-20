#!/usr/bin/python3
"""
lists the first state
"""
from model_state import State, Base
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}\
            @localhost/{}".format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).order_by(State.id).first()
    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))
