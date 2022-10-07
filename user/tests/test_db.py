from utils import get_client
from django.http import HttpResponse
from user.views import userDB
from django.test import TransactionTestCase

class Testdb(TransactionTestCase):


    def test_insert_db(self):

        data =  {"username": "John",
                 "unityid" : "jdwyer",
                 "fname" : "John",
                 "lname" : "Dwyer",
                 "email" : "jdwyer@ncsu.edu",
                 "password" : "jd45678",
                 "phone" : "987657890"}


        self.assertEqual(userDB.insert_one(data),True)