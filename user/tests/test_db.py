from utils import get_client
from django.http import HttpResponse
from user.views import userDB

from django.test import SimpleTestCase

class Testdb(SimpleTestCase):



    def test_insert_db(self):

        data =  {"username": "John",
                 "unityid" : "jdwyer",
                 "fname" : "John",
                 "lname" : "Dwyer",
                 "email" : "jdwyer@ncsu.edu",
                 "password" : "jd45678",
                 "phone" : "987657890"}

        id = userDB.insert_one(data).inserted_id
        return id
        # self.assertEqual(userDB.insert_one(data),True)

    def test_find_db(self):
        id = self.test_insert_db()
        result= userDB.find_one({'_id':id})
        print("res is",result)
        self.assertEqual(result['_id'], id)

    def test_delete_db(self):
        id = self.test_insert_db()
        userDB.delete_one({'_id':id})

