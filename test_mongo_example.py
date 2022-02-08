"""
A few tests for the mongo_example code

These use pytet and pytest fixtures

You can do similar things with unittest fixtures (setUp() methods)
"""

import pytest

from mongo_example import start_mongo, DirectorCollection

CLIENT = start_mongo()

@pytest.fixture
def empty_db():
    """
    provides an empty database to use for testing

    NOTE: you can have multiple databases in one mongo instance
          So we can use one for testing that's separte from the
          operational one
    """
    CLIENT.drop_database('test_database')

    # now create it again
    return CLIENT.test_database

@pytest.fixture
def full_db():
    """
    provides an empty database to use for testing

    NOTE: you can have multiple databases in one mongo instance
          So we can use one for testing that's separte from the
          operational one
    """
    CLIENT.drop_database('test_database')

    # now create it again
    db = CLIENT.test_database

    # and populate it

    return db


def init_director_collection_empty(empty_db):
    """
    really a test of the fixture
    """
    dircol = DirectorCollection(empty_db)

    assert len(dircol) == 0


def init_director_collection_full(empty_db):
    """
    really a test of the fixture
    """
    dircol = DirectorCollection(empty_db)

    assert len(dircol) == 3


def test_search_director(full_db):
    pass


def test_add_director(empty_db):
    pass

