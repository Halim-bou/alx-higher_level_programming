#!/usr/bin/python3
"""
Write a script that lists all states from the
database hbtn_0e_0_usa when name matches the srguments
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute(
            "SELECT * FROM states WHERE name = '{:s}'\
                    ORDER BY id ASC".format(argv[4]))
    states = cursor.fetchall()
    for state in states:
        if state[1] == argv[4]:
            print(state)
    cursor.close()
    db.close()
