#!/usr/bin/env python3
""" pymongo list"""
def list_all(mongo_collection):
    """ List all elements in a collection """
    return [doc for doc in mongo_collection.find()]
