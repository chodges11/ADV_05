"""
main driver for a simple social network project
"""
# pylint: disable = import-error
# pylint: disable=unspecified-encoding
# pylint: disable = invalid-name

import csv
from pymongo import MongoClient
import users as u
import user_status as us


class MongoDBConnectionManager():
    """MongoDB Connection."""

    def __init__(self, hostname='127.0.0.1', port=27017):
        """Initialize the MongoDB object."""
        self.hostname = hostname
        self.port = port
        self.client = None

    def __enter__(self):
        self.client = MongoClient(self.hostname, self.port)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.client.close()


def init_user_collection(db):
    """
    Creates and returns a new instance of UserCollection
    """
    return u.UserCollection(db)


def init_status_collection(db):
    """
    Creates and returns a new instance of UserStatusCollection
    """
    return us.UserStatusCollection(db)


def load_users(filename, user_collection):
    """
    Opens a CSV file with user data and
    adds it to an existing instance of
    UserCollection

    Requirements:
    - If a user_id already exists, it
    will ignore it and continue to the
    next.
    - Returns False if there are any errors
    (such as empty fields in the source CSV file)
    - Otherwise, it returns True.
    """
    try:
        with open(filename, newline='') as read_obj:
            csv_dict_reader = csv.DictReader(read_obj)
            for row in csv_dict_reader:
                user_collection.add_user(row["USER_ID"],
                                         row["NAME"],
                                         row["LASTNAME"],
                                         row["EMAIL"]
                                         )
        return True

    except OSError as error:
        print(f"{type(error)}: {error}")
        return False


def load_status_updates(filename, status_collection):
    """
    Opens a CSV file with status data and adds it to an existing
    instance of UserStatusCollection

    Requirements:
    - If a status_id already exists, it will ignore it and continue to
      the next.
    - Returns False if there are any errors(such as empty fields in the
      source CSV file)
    - Otherwise, it returns True.
    """
    try:
        with open(filename, newline='') as read_obj:
            csv_dict_reader = csv.DictReader(read_obj)
            for row in csv_dict_reader:
                status_collection.add_status(row["STATUS_ID"],
                                             row["USER_ID"],
                                             row["STATUS_TEXT"]
                                             )
        return True

    except OSError as error:
        print(f"{type(error)}: {error}")
        return False


def add_user(user_id, email, user_name, user_last_name, user_collection):
    """
    Creates a new instance of User and stores it in user_collection
    (which is an instance of UserCollection)

    Requirements:
    - user_id cannot already exist in user_collection.
    - Returns False if there are any errors (for example, if
      user_collection.add_user() returns False).
    - Otherwise, it returns True.
    """
    while user_collection.add_user(user_id,
                                   user_name,
                                   user_last_name,
                                   email
                                   ):
        return True
    return False


def update_user(user_id, email, user_name, user_last_name, user_collection):
    """
    Updates the values of an existing user

    Requirements:
    - Returns False if there are any errors.
    - Otherwise, it returns True.
    """
    while user_collection.update_user(user_id,
                                      user_name,
                                      user_last_name,
                                      email
                                      ):
        return True
    return False


def delete_user(user_id, user_collection):
    """
    Deletes a user from user_collection.

    Requirements:
    - Returns False if there are any errors (such as user_id not found)
    - Otherwise, it returns True.
    """
    while user_collection.delete_user(user_id):
        return True
    return False


def search_user(user_id, user_collection):
    """
    Searches for a user in user_collection(which is an instance of
    UserCollection).

    Requirements:
    - If the user is found, returns the corresponding User instance.
    - Otherwise, it returns None.
    """
    user_search_results = user_collection.search_user(user_id)
    if user_search_results is not None:
        return user_search_results

    return None


def add_status(status_id, user_id, status_text, status_collection):
    """
    Creates a new instance of UserStatus and stores it in
    status_collection(which is an instance of UserStatusCollection)

    Requirements:
    - status_id cannot already exist in status_collection.
    - Returns False if there are any errors (for example, if
      user_collection.add_status() returns False).
    - Otherwise, it returns True.
    """
    while status_collection.add_status(status_id,
                                       user_id,
                                       status_text
                                       ):
        return True
    return False


def update_status(status_id, user_id, status_text, status_collection):
    """
    Updates the values of an existing status_id

    Requirements:
    - Returns False if there are any errors.
    - Otherwise, it returns True.
    """
    while status_collection.update_status(status_id,
                                          user_id,
                                          status_text
                                          ):
        return True
    return False


def delete_status(status_id, status_collection):
    """
    Deletes a status_id from user_collection.

    Requirements:
    - Returns False if there are any errors (such as status_id not found)
    - Otherwise, it returns True.
    """
    while status_collection.delete_status(status_id):
        return True
    return False


def search_status(status_id, status_collection):
    """
    Searches for a status in status_collection

    Requirements:
    - If the status is found, returns the corresponding
    UserStatus instance.
    - Otherwise, it returns None.
    """
    status_search_results = status_collection.search_status(status_id)
    if status_search_results is not None:
        return status_search_results
    return None
