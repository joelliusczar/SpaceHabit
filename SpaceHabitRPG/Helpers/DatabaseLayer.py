import ConfigLayer
from pymongo import MongoClient
import pymongo

"""
    This is a wrapper for interaction with the database. Each of these methods
    can be overridden to connect to a different db.
"""

connection = None

def get_open_connection():
    """
        wrappper around the opening of the connection to the db
    """
    return MongoClient(ConfigLayer.get_url(), int(ConfigLayer.get_port()))
    

def open_conn():
    """
        Checks if there is already an open db connection. If not then it opens
        one. Either way, it returns the open db connection.
    """
    global connection
    if connection is None:
        connection = get_open_connection()
    return connection


def get_table(tableName):
    """
        gets the dataset associated with the given name.

        args:
            tableName: 
                name of the dataset that is wanted by the caller

        returns:
            a dataset upon which futher inquries can be done.
    """
    open_conn()
    db = connection.spacehabit
    return db[tableName]


def get_thing_by_id(id,tableName):
    """
        This is a wrapper method to get a single item from the database that
        is associated with the given id.

        args:
            id: 
                this is a primary key for an item in the database
            tableName: 
                this is the name of the dataset that is expected to have
                the item we're looking for.

        returns:
            a dict with an _id field that matches id
    """
    collection = get_table(tableName)
    return collection.find_one({'_id':id})


def insert_thing(stuff, tableName):
    """
        this is a wrapper method for inserting an item into the db

        args:
            stuff: 
                this will be a dict. Ideally this will have most of the
                same properties that the rest of the items in this dataset has.
            tableName: 
                this is the name of the dataset that we're inserting
                our item into.

        returns:
            the primary key of the newly inserted item.
    """
    collection = get_table(tableName)
    id = collection.insert_one(stuff).inserted_id
    return id


def update_thing_by_id(id,tableName,changes):
    """
        This is a wrapper method for updating a single item in our db.

        args:
            id: 
                this is a primary key for an item in the database
            tableName: 
                this is the name of the dataset that is expected to have
                the item we're looking for.
            changes: 
                this will be a dict. Each field in this dict will have a value
                that overwrites the old value for that field for that item
                in the db
    """
    collection = get_table(tableName)
    collection.update(
            {'_id': id},
            {
            '$set': changes,    
            }
        )


def delete_thing_by_key(key,tableName):
    """
        Removes a particular item from the database

        args:
            key:
                primary key of the item that we want to remove from the db
            tableName:
                name of the dataSet that has the item that we want to remove
    """
    collection = get_table(tableName)
    collection.remove({'_id':key})

def get_sorted_stuff_by_search(searchForDict,tableName,sortByList = None,limit=10000):
    """
        gets a collection of items from the database that matches a given
        search criteria and then sorts it by some fields given to it

        args:
            searchForDict:
                this will be a dict of what to search the database for. 
                To be returned by this method, the item in the database
                must have contain all of the keys in searchForDict and 
                paired values must also match. 
                Read the mongoDB tutorial on find for clarification.
            tableName:
                name of the dataset that we are getting items from
            sortByList:
                this will be a list of tuples.
                Each tuple in the list, must have two values. The first is the
                name of the field that we are sorting by. The second value is
                either 1 or -1(pymongo.ASCINDING, pyongo.DESCINDING)
                This will tell the database to sort the values in increasing
                or decreasing order.
            limit:
                this is the maximum number of records to return


        returns:
            Right now, this returns some sort of mongoDB collection, but I am
            going to change this to return a wrapper object with skip and limit
            methods.

    """
    collection = get_table(tableName)
    findResult = collection.find(searchForDict)
    if sortByList:
        return findResult.sort(sortByList).limit(limit)
    else:
        return findResult.limit(limit)


def get_count_of_stuff_search(searchForDict,tableName):
    """
        This is a wrapper method for getting the count of items in a particular
        dataset.

        args:
            searchForDict:
                this will be a dict of what to search the database for. 
                To be counted by this method, the item in the database
                must have contain all of the keys in searchForDict and 
                paired values must also match. 
                Read the mongoDB tutorial on find for clarification.
            tableName:
                name of the dataset that we are counting items from

        returns:
            The count of items from our given dataset and that meet our 
            conditions
    """
    collection = get_table(tableName)
    return collection.find(searchForDict).count()