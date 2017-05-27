#coding:utf-8
from selenium import webdriver
import time
class QQDailyHot(object):
	def __init__(self):
		self.webdriver=webdriver.Chrome()
		self.webdriver.maximize_window()
		self.webdriver.get("http://www.qq.com/")
		self.url=self.get_url()
		self.title=self.get_title()
		self.content=self.get_content()
	def by_Xpath(self,xpath):
		return self.webdriver.find_element_by_xpath(xpath)
	def by_Id(self,id):
		return self.webdriver.find_element_by_id(id)
	def by_Name(self,name):
		return self.webdriver.find_element_by_name(name)
	def quit(self):
		self.webdriver.quit()
	def get_url(self):
		time.sleep(4)
		return self.by_Xpath("//h3[@id='todaytop']/a").get_attribute('href')
	def get_title(self):
		self.webdriver.get(self.url)
		time.sleep(3)
		title=self.by_Id("sharetitle").text
		return title
	def get_content(self):
		self.webdriver.get(self.url)
		time.sleep(3)
		content=self.by_Id("articleContent").get_attribute("innerHTML")
		return content
	def post_content(self,content):
		content = content.strip()
		js='document.getElementById("content_ifr").contentWindow.document.body.innerHTML=\'%s\'' %(content)
		#print js
		self.webdriver.execute_script(js)
	def post_title(self,title):
		self.by_Name("post_title").send_keys(title)
	def login(self,username,password):
		self.webdriver.get("http://localhost/wordpress/wordpress/wp-login.php")
		self.by_Id("user_login").send_keys(username)
		self.by_Id("user_pass").send_keys(password)
		self.by_Id("wp-submit").click()
	def post_title_content(self):
		#调用登录模块
		self.login("admin","123456")
		self.webdriver.get("http://localhost/wordpress/wordpress/wp-admin/post-new.php")
		time.sleep(3)
		#print self.title

		self.post_title(self.title)
		time.sleep(3)
		self.post_content(self.content)
		time.sleep(3)
		self.by_Name("publish").click()
		time.sleep(3)
		self.quit()
if __name__ == '__main__':
	day=QQDailyHot()
	day.post_title_content()
