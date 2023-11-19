#!/usr/bin/python3
from sys import argv
import sqlalchemy
import MySQLdb
from model_state import State, Base
"""
script that prints the first State object from the database hbtn_0e_6_usa
"""


if __name__ == "__main__":
    mysql = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"
    db = sqlalchemy.create_engine(mysql)
    Base.metadata.create_all(db)
    session_fake = sqlalchemy.orm.sessionmaker(bind=db)
    session = session_fake()
    first_state = session.query(State).first()
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")
