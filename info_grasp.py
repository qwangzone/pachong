#coding:utf-8
from selenium import webdriver
import time
class Info_Grasp(object):
    def __init__(self):
        self.dr=webdriver.Chrome()
        self.dr.maximize_window()
        self.info_url="http://www.infoq.com/cn/Testing/news/"
        self.blog_url="http://localhost/wordpress/wordpress/wp-login.php"
        self.url=self.get_url()
        self.title,self.content=self.get_title_content()
    def by_Id(self,id):
        return self.dr.find_element_by_id(id)
    def by_Name(self,name):
        return self.dr.find_element_by_name(name)
    def get_url(self):
        self.dr.get(self.info_url)
        ares=self.by_Id("content")
        news_ares=ares.find_elements_by_css_selector("div[class^='news_type_block']>h2>a")
        url_list=[]
        for i in news_ares:
            url_list.append(i.get_attribute("href"))
        return url_list
    def get_title_content(self):
        titles=[]
        contents=[]
        for url in self.url:
            self.dr.get(url)
            time.sleep(2)
            title=self.dr.find_element_by_css_selector("h1.general").text
            titles.append(title)
            content=self.dr.find_element_by_css_selector("div.text_info").get_attribute("innerHTML")
            contents.append(content)
        return titles,contents
    def post_title(self,title):
		self.by_Name("post_title").send_keys(title)
    def post_content(self,content):
        content = content.strip().replace("'","\"").replace("\n","<br/>")#删除content中的空白符（包括'\n', '\r',  '\t',  ' ')
        js='document.getElementById("content_ifr").contentWindow.document.body.innerHTML=\'%s\'' %(content)
        self.dr.execute_script(js)
    def login(self,username,password):
        self.dr.get("http://localhost/wordpress/wordpress/wp-login.php")
        self.by_Id("user_login").send_keys(username)
        self.by_Id("user_pass").send_keys(password)
        time.sleep(3)

        self.by_Id("wp-submit").click()

    def post_title_content(self):
        self.login("admin","123456")
        current_url=self.dr.current_url
        if current_url != "http://localhost/wordpress/wordpress/wp-admin/":
            self.login("admin","123456")
        else:
            pass

        for i in range(len(self.title)):
            self.dr.get("http://localhost/wordpress/wordpress/wp-admin/post-new.php")
            self.post_title(self.title[i])
            time.sleep(3)
            self.post_content(self.content[i])
            time.sleep(3)
            self.by_Name("publish").click()
            time.sleep(3)
        print len(self.content)
        self.dr.quit()
if __name__ == '__main__':
    info=Info_Grasp()
    info.post_title_content()
