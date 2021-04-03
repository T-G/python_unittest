import unittest
from selenium import webdriver
'''
Unit Test: Assertions Test
1.  Assertion is a verification for the test case 
    to evaluate some item on the execution.
    It helps in report generation, based on the assertions 
    the test execution report will be generated.
    
2.  There are few assertion which accepts all the values and 
    few assertions will accept only numeric values
    
assertIsNone:   This method verifies whether given value or expression results in None
                or not, if the result is none then unittest will pass the test case

assertIsNotNone:This method verifies whether given values or expression is not None
                or not, if the result is none then unittest will fail the test case
'''

class AppTesting(unittest.TestCase):
    browser_driver_location = '/home/theo/Workspace/browsersDriver/chromedriver'
    url = 'https://www.google.com/'

    def testname(self):
        self.driver = webdriver.Chrome(executable_path=self.browser_driver_location)
        self.assertIsNone(self.driver)


if __name__ == '__main__':
    unittest.main()