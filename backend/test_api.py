import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from database.models import setup_db, Show, Movie, Actor

#class ApiTestCases(unittest.TestCase):
#    def setUp(self):
#        self.