#!/usr/bin/python3
"""Script that prints the State object with the name passed as argument.

This script connects to a MySQL database using SQLAlchemy ORM and
searches for a State object whose name matches the argument provided.
If the state is found, its id is printed. Otherwise, "Not found" is displayed.

The search uses SQLAlchemy's filter() method with an equality check,
which is safe against SQL injection.

Usage:
    ./10-model_state_my_get.py <mysql_username> <mysql_password>
                               <database_name> <state_name>

Arguments:
    mysql_username (str): MySQL username for authentication.
    mysql_password (str): MySQL password for authentication.
    database_name (str): Name of the MySQL database to connect to.
    state_name (str): Name of the state to search for.

Output:
    Prints the id of the matching State, or "Not found" if no match exists.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(
        State.name == sys.argv[4]
    ).first()

    if state is None:
        print("Not found")
    else:
        print(state.id)

    session.close()
