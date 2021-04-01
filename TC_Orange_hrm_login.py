from selenium import webdriver
import HtmlTestRunner
import unittest

'''
Test Case: OrangeHRM login test
1. Launch Browser
2. Verify home page title
3. Verify Login
4. Close browser
setUpClass() will execute before all the steps are being executed
tearDownClass() will execute only one time after completion of test method
'''

class test_OrangeHRMTest(unittest.TestCase):
