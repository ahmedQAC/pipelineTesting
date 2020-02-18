from selenium import webdriver
import unittest

class DjangoFunctionalCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(executable_path='./geckodriver')

    def test_first(self):
        self.browser.get('http://google.com')
        assert self.browser.page_source.find('google')
    
    def tearDown(self):
        self.browser.quit()

# browser = webdriver.Firefox()
# browser.get('http://google.com')

# assert browser.page_source.find('google')

if __name__ == '__main__':
    unittest.main()