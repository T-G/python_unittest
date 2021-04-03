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
    
assertEqual :   It compares the first parameter with the second parameter,
                if both matches the unittest will continue with the remaining
                execution but if both the values are different then unit test
                fails the testcase
'''

class AppTesting(unittest.TestCase):
    browser_driver_location = '/home/theo/Workspace/browsersDriver/chromedriver'
    url = 'https://www.google.com/'

    def testname(self):
        self.driver = webdriver.Chrome(executable_path=self.browser_driver_location)
        self.driver.get(self.url)

        titleOfWebPage = self.driver.title

        # Expecting title = Google
        self.assertEqual('Google12', titleOfWebPage, 'Webpage title is not same')


if __name__ == '__main__':
    unittest.main()