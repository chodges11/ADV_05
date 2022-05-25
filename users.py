"""
Classes for user information for the social network project
"""
# pylint: disable=R0903

import sys
from loguru import logger
from pymongo.errors import DuplicateKeyError


class UserCollection():
    """
    Contains a collection of Users objects
    """

    def __init__(self, database):
        self.database = database
        self.users_coll = database['users']
        self.status_coll = database['user_status']
        logger.add(sys.stderr, format="{time} {level} {message}",
                   filter="my_module", level="INFO")
        logger.add("log_file.log")
        logger.info('Created New User Collection')

    def add_user(self, user_id, user_name, user_last_name, email):
        """
        Adds a new user to the collection
        """
        new_user = {"_id": user_id, "user_name": user_name,
                    "user_last_name": user_last_name, "email": email}
        try:
            self.users_coll.insert_one(new_user)
            logger.info('Add User')
            return True

        except DuplicateKeyError as error:
            logger.info(f"{type(error)}: {error}")
            logger.info('Did Not Add User: user already exists')
            return False

    def update_user(self, user_id, user_name, user_last_name, email):
        """
        Updates an existing user
        """
        if self.search_user(user_id) is not None:
            user_update = {
                "_id": user_id,
                "user_name": user_name,
                "user_last_name": user_last_name,
                "email": email
            }
            updates = {"$set": user_update}
            self.users_coll.update_one({"_id": user_id}, updates)
            logger.info('Updated User')
            return True
        return False

    def delete_user(self, user_id):
        """
        Deletes an existing user
        """
        if self.search_user(user_id) is not None:
            # Didn't get the status deletions aspect on my own, but your
            # example reminded me that non-relational DBs need this extra step.
            # Thanks!
            self.status_coll.delete_many({"_id": user_id})  # This line
            self.users_coll.delete_one({"_id": user_id})
            logger.info('Deleted User and their statuses.')
            return True
        logger.info('Did Not Delete User: user does not exist: ')
        return False

    def search_user(self, user_id):
        """
        Searches for user data
        """
        if not self.users_coll.find_one({"_id": user_id}):
            # Fails if the user does not exist
            logger.info(
                'Failed Search For User in Database: user does not exist'
            )
            return None
        logger.info('Successfully searched for User.')
        return self.users_coll.find_one({"_id": user_id})
