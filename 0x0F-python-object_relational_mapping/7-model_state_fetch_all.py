#!/usr/bin/python3
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
"""
script that lists all State objects from the database hbtn_0e_6_usa
"""


if __name__ == "__main__":
    myeng = 'mysql+mysqldb://{}:{}\
            @localhost/{}'.format(argv[1], argv[2], argv[3])
    db = create_engine(myeng)
    Base.metadata.create_all(db)
    Session = sessionmaker(bind=db)
    session = Session()
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
    session.close()