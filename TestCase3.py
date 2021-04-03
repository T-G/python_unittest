import unittest

'''
setUp() and tearDown() method demo
1. setUp() method will execute multiple times before executing each test method in a class
2. tearDown() method will execute multiple times after executing each test method in a class
3. setUpClass() method will execute only one time before executing all the methods in a class
4. tearDownClass() method will execute only one time after executing all the methods in a class
5. setUpModule() method will execute only one time before the module is started
6. tearDownModule() method will execute only one time after the module is completed
note: setUpModule and tearDownModule should be placed outside of the class, because these method are
module level
'''

def setUpModule():
    print('setUpModule')

def tearDownModule():
    print('tearDownModule')

class AppTesting(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Open Application')

    @classmethod
    def tearDownClass(cls):
        print('Close Application')

    @classmethod
    def setUp(self):
        print('This is login test')

    @classmethod
    def tearDown(self):
        print('This is logout test')

    def test_search(self):
        print('This is search test')

    def test_advancedsearch(self):
        print('This is advance search test')

    def test_prepaidRecharge(self):
        print('This is prepaidRecharge test')

    def test_postpaidRecharge(self):
        print('This is postpaidRecharge test')



if __name__ == '__main__':
    unittest.main()