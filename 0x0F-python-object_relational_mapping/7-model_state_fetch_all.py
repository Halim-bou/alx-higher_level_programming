#!/usr/bin/python3
from sys import argv
import sqlalchemy
import MySQLdb
from model_state import State, Base
"""
script that lists all State objects from the database hbtn_0e_6_usa
"""


if __name__ == "__main__":
    mysql = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"
    db = sqlalchemy.create_engine(mysql)
    Base.metadata.create_all(db)
    session_fake = sqlalchemy.orm.sessionmaker(bind=db)
    session = session()
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
    session.close()
