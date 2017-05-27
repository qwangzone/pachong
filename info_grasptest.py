#coding:utf-8
from selenium import webdriver
import time
class Info_Test(object):
    def __init__(self):
        self.dr=webdriver.Chrome()
        self.dr.maximize_window()
        self.url="http://www.infoq.com/cn/news/2017/01/alibaba-yunxiao-cicd-devops"
        self.title,self.content=self.get_title_content()
    def get_title_content(self):
        self.dr.get(self.url)
        title=self.dr.find_element_by_css_selector("h1.general").text
        content=self.dr.find_element_by_css_selector("div.text_info").get_attribute("innerHTML")
        return title,content
    def by_Id(self,id):
        return self.dr.find_element_by_id(id)
    def by_Name(self,name):
        return self.dr.find_element_by_name(name)
    def post_title(self,title):
        self.dr.find_element_by_name("post_title").send_keys(title)
    def post_content(self,content):
        content=content.strip().replace("'","\"").replace("\n","<br/>")
        js='document.getElementById("content_ifr").contentWindow.document.body.innerHTML=\'%s\'' %(content)
        self.dr.execute_script(js)
    def login(self,username,password):
        self.dr.get("http://localhost/wordpress/wordpress/wp-login.php")
        self.by_Id("user_login").send_keys(username)
        time.sleep(2)
        self.by_Id("user_pass").send_keys(password)
        time.sleep(3)
        self.by_Id("wp-submit").click()
    def post_title_content(self):
        #调用登录模块
        self.login("admin","123456")
        self.dr.get("http://localhost/wordpress/wordpress/wp-admin/post-new.php")
        time.sleep(3)
        #print self.title
        self.post_title(self.title)
        time.sleep(3)
        self.post_content(self.content)
        time.sleep(3)
        self.by_Name("publish").click()
        time.sleep(3)
        self.dr.quit()
if __name__ == '__main__':
    infotest=Info_Test()
    infotest.post_title_content()
