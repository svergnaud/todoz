from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        '''
        This method is called before each test
        '''
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        '''
        This method is called after each test
        We ensure we close the browser
        '''
        self.browser.quit()

    def test_content(self):
        '''
        This is our actual test !
        '''

        # Chloe heard about an awesome new website
        # and wants to check it out
        self.browser.get('http://localhost:8000')

        # Chloe has a sharp eye and notice the title !
        #self.assertIn('Django', self.browser.title)
        self.assertIn('ToDoz', self.browser.title)
