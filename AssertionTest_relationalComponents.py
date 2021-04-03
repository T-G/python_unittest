import unittest
'''
Unit Test: Relational Comparison 
assertGreater: It verifies whether first parameter is greater than second parameter or not.
assertGreaterEqual: It verifies whether first parameter is greater or
                    equal to second parameter.
assertLess: It verifies whether first parameter is lesser than second parameter or not.
assertLessEqual: It verifies whether first parameter is greater than second parameter or not.

'''

class AppTest(unittest.TestCase):
    def testName(self):
        # assertGreater
        #self.assertGreater(100,10)

        # assertGreaterEqual
        #self.assertGreaterEqual(100, 20)

        # assertLess
        #self.assertLess(100,10)

        # assertLessEqual
        self.assertLessEqual(100,100)

if __name__ == '__main__':
    unittest.main()