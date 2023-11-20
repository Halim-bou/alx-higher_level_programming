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
    new_st = State(name='Louisiana')
    session.add(new_st)
    state = session.query(State).filter_by(name='Louisiana').first()
    print(str(state.id))
    session.commit()
