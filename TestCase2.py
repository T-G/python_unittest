import unittest
from selenium import webdriver
'''
Test Case: Get title of the Google home page
1. Launch google browser
2. Print/ verify the title of the page
'''

class SearchEnginesTest(unittest.TestCase):
    browser_driver_location = '/home/theo/Workspace/browsersDriver/chromedriver'

    def test_Google(self):
        self.url = 'https://www.google.com/'
        self.driver = webdriver.Chrome(executable_path=self.browser_driver_location)
        self.driver.get(self.url)
        print(f'Title of the page is: {self.driver.title}')
        self.driver.close()

    def test_Bing(self):
        self.url = 'https://bing.com'
        self.driver = webdriver.Chrome(executable_path=self.browser_driver_location)
        self.driver.get(self.url)
        print(f'Title of the page is: {self.driver.title}')
        self.driver.close()


if __name__ == '__main__':
    unittest.main()