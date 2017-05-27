#coding:utf-8
from selenium import webdriver
import unittest
import time,sys,csv
import HTMLTestRunner
#reload(sys)
#sys.setdefaultencoding('utf-8')
class Login(unittest.TestCase):
	def setUp(self):
		self.driver=webdriver.Chrome()
		self.driver.get("http://localhost/wordpress/wordpress/wp-login.php")
		self.driver.maximize_window()
	def tearDown(self): 
		self.driver.quit()
	def by_Id(self,id):
		return self.driver.find_element_by_id(id)
	def by_Name(self,name):
		return self.driver.find_element_by_name(name)
	def by_Class_name(self,classname):
		return self.driver.find_element_by_class_name(classname)
	def switch_Iframe(self,id):
		self.driver.switch_to_iframe(id)
	def write_content(self,content):
		js="document.getElementById('content_ifr').contentWindow.document.body.innerHTML='%s'"%(content)
		self.driver.execute_script(js)
	def write_title(self,title):
		self.by_Name("post_title").send_keys(title)
	def title_verify(self):
		self.driver.get("http://localhost/wordpress/wordpress/wp-admin/edit.php")
		title_text=self.by_Class_name("row-title").text
		return title_text
	def login(self,username,password):
		self.by_Id("user_login").send_keys(username)
	    self.by_Id("user_pass").send_keys(password)
		self.by_Id("wp-submit").click()
	def post_title_content(self,title,content):
		self.driver.get("http://localhost/wordpress/wordpress/wp-admin/post-new.php")
		time.sleep(3)
		self.write_title(title)
		self.write_content(content)
		time.sleep(3)
		self.by_Name("publish").click()
		time.sleep(3)
	def test_post(self):
		#调用登录模块
		self.login("admin","123456")
		time.sleep(3)
		f=open('test.csv','r')
		reader=csv.reader(f)
		for title,content in reader:
			self.post_title_content(title,content)
			print self.title_verify()
			self.assertEqual(title,self.title_verify())
			time.sleep(3)

if __name__ == '__main__':
	unittest.main()
