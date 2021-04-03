import unittest

'''
Unit Test: Skip Test
1. Skip Test
2. Skip Test with reason
3. Skip Test based on condition
'''

class AppTesting(unittest.TestCase):

    @unittest.SkipTest # decorator
    def test_search(self):
        print('This is search test')

    @unittest.skip('I am skipping this test method because it is not ready')
    def test_advancedsearch(self):
        print('This is advance search test')

    @unittest.skipIf(1==1, 'Numbers are not equal') # condition
    def test_prepaidRecharge(self):
        print('This is pre-paid Recharge test')

    def test_postpaidRecharge(self):
        print('This is post-paid Recharge test')

    def test_loginbyGmail(self):
        print('This is login in by gmail test')

    def test_loginbyTwitter(self):
        print('This is login in by twitter test')

if __name__ == '__main__':
    unittest.main()