import unittest
'''
Unit Test: Assertions Test
1.  Assertion is a verification for the test case 
    to evaluate some item on the execution.
    It helps in report generation, based on the assertions 
    the test execution report will be generated.
    
2.  There are few assertion which accepts all the values and 
    few assertions will accept only numeric values
    
assertIn :  This method verifies whether the first element is present in the second element, 
            if the first element is present in the second element then the test is passed
            otherwise test failed.
            
saaserNotIn: This method verifies whether the first element is not present in the second element, 
            if the first element is present in the second element then the test will fail.
            otherwise test failed otherwise passed.
            These two methods will be helpful when you want to verify presence of a value
            in a list, tuple, set and dictionary.
            T
'''

class AppTest(unittest.TestCase):
    def testName(self):
        list = ('python', 'selenium', 'java')

        self.assertIn('python1', list) # failed

if __name__ == '__main__':
    unittest.main()