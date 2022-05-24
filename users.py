"""
Classes for user information for the social network project
"""
# pylint: disable=R0903

import sys
from loguru import logger


class Users():
    """
    Contains user information
    """

    def __init__(self, user_id, email, user_name, user_last_name):
        self.user_id = user_id
        self.email = email
        self.user_name = user_name
        self.user_last_name = user_last_name
        logger.add(sys.stderr, format="{time} {level} {message}",
                   filter="my_module", level="INFO")
        logger.add("log_file.log")
        logger.info('Created Users')


class UserCollection():
    """
    Contains a collection of Users objects
    """

    def __init__(self):
        self.database = {}
        logger.add(sys.stderr, format="{time} {level} {message}",
                   filter="my_module", level="INFO")
        logger.add("log_file.log")
        logger.info('Created User Collection')

    def add_user(self, user_id, email, user_name, user_last_name):
        """
        Adds a new user to the collection
        """

        if user_id in self.database:
            # Rejects new user if user_id already exists
            logger.info('Did Not Add User: user_id already exists')
            return False
        new_user = Users(user_id, email, user_name, user_last_name)
        self.database[user_id] = new_user
        logger.info('Add User')
        return True

    def update_user(self, user_id, email, user_name, user_last_name):
        """
        Updates an existing user
        """

        if user_id not in self.database:
            # Rejects update if the user_id does not exist
            logger.info('Did Not Update User: user_id does not exist')
            return False
        self.database[user_id].email = email
        self.database[user_id].user_name = user_name
        self.database[user_id].user_last_name = user_last_name
        logger.info('Updated User')
        return True

    def delete_user(self, user_id):
        """
        Deletes an existing user
        """
        if user_id not in self.database:
            # Fails if user does not exist
            logger.info(
                'Did Not Delete User: user does not exist: ')
            return False
        del self.database[user_id]
        logger.info('Deleted User')
        return True

    def search_user(self, user_id):
        """
        Searches for user data
        """
        if user_id not in self.database:
            # Fails if the user does not exist
            logger.info(
                'Failed Search For User in Database: '
                'user does not exist')
            return Users(None, None, None, None)
        logger.info('Successfully Searched for User Status')
        return self.database[user_id]
