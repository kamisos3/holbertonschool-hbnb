#!/usr/bin/python3
"""Instance created for facade"""

from app.services.facade import HBNBFacade

facade = HBNBFacade()
""" This instance will be used as a singleton to make sure that only
    one HBNBFacade class is creted in the whole application.
"""
