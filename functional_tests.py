from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		
	def tearDown(self):
		self.browser.quit()
		
	def test_can_start_a_list_and_retrieve_it_later(self):
		## check out apps homepage
		self.browser.get('http://localhost:8000')
		
		## title and header mention to-do
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)
		
		## She is invited to enter a to-do item straight away
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)
		
		## She types 'buy peacock feathers' into a text box
		inputbox.send_keys('Buy peacock featehrs')
		
		## When she hits enter, the page updates the list 
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)
		
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1: Buy peacock featehrs' for row in rows),
			"New to-do item did not appear in table"
		)
		
		## The box is still there
		## another item is entered in the list
		self.fail('Finish the test!')
		
		## the page updates again, now both items are in the list
		[...]
		
if __name__ == '__main__':
	unittest.main(warnings='ignore')
