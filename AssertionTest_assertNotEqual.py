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

assertNotEqual: This method compares the given two parameters, if both parameters
                are not same then unittest passes the test case, but if both 
                parameters are same then the unittest fails the test case  
'''

class AppTesting(unittest.TestCase):
    browser_driver_location = '/home/theo/Workspace/browsersDriver/chromedriver'
    url = 'https://www.google.com/'

    def testname(self):
        self.driver = webdriver.Chrome(executable_path=self.browser_driver_location)
        self.driver.get(self.url)

        titleOfWebPage = self.driver.title

        # Expecting title = Google
        self.assertNotEqual('Google12', titleOfWebPage, 'Webpage title is not same')


if __name__ == '__main__':
    unittest.main()