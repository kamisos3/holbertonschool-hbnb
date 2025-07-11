#!/usr/bin/python3
"""Defines environment-specific settings"""
import os

class Config:
    SECRET_KEY = 'hbnb-project-pt3'
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'

class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
