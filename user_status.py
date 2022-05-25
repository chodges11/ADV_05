"""
classes to manage the user status messages
"""
# pylint: disable=R0903

import sys
from loguru import logger
from pymongo.errors import DuplicateKeyError


class UserStatusCollection():
    """
    Collection of UserStatus messages
    """

    def __init__(self, database):
        self.database = database
        self.users_coll = database['users']
        self.status_coll = database['user_status']
        logger.add(sys.stderr, format="{time} {level} {message}",
                   filter="my_module", level="INFO")
        logger.add("log_file.log")
        logger.info('Created New User Status Collection')

    def add_status(self, status_id, user_id, status_text):
        """
        add a new status message to the collection
        """
        if self.users_coll.find_one({"_id": user_id}):
            new_status = {"_id": status_id, "user_id": user_id,
                          "status_text": status_text}
            try:
                self.status_coll.insert_one(new_status)
                logger.info('Add Status')
                return True

            except DuplicateKeyError as error:
                logger.info(f"{type(error)}: {error}")
                logger.info('Did Not Add User: status already exists')
                return False
        logger.info('User does not exist, so status can not be added.')
        return False

    def update_status(self, status_id, user_id, status_text):
        """
        Updates a status message
        """
        if self.search_status(status_id) is not None:
            status_update = {"_id": status_id, "user_id": user_id,
                             "status_text": status_text}
            updates = {"$set": status_update}
            self.status_coll.update_one({"_id": status_id}, updates)
            logger.info('Updated Status')
            return True
        return False

    def delete_status(self, status_id):
        """
        deletes the status message with id, status_id
        """
        if self.search_status(status_id) is not None:
            self.status_coll.delete_one({"_id":status_id})
            logger.info('Deleted Status.')
            return True
        logger.info('Did Not Delete Status: status does not exist: ')
        return False

    def search_status(self, status_id):
        """
        Find and return a status message by its status_id
        """
        if not self.status_coll.find_one({"_id": status_id}):
            # Fails if the status does not exist
            logger.info(
                'Failed Search For Status in Database: '
                'status does not exist'
            )
            return None
        logger.info('Successfully searched for Status')
        return self.status_coll.find_one({"_id": status_id})
