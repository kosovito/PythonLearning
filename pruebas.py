def say_hello(name):
    return f"Hello, {name}!"
def say_hello():
    return "Hello there!"


import unittest 
from pruebas import say_hello

# These example test cases are editable, feel free to add
# your own tests to debug your code.
class Test(unittest.TestCase):
    def test_should_say_hello(self):
        self.assertEqual(say_hello("Qualified"), "Hello, Qualified!")
    def test_empty(self):
        self.assetEqual(say_hello(), "Hello there!")