#coding:utf-8
from selenium import webdriver
import time
"""抓取微博24小时热门话题的前15个(http://d.weibo.com/100803?cfs=&Pl_Discover_Pt6Rank__5_filter=hothtlist_type%3D1#_0)，
注意需要翻页，抓取的内容请保存至txt文件中，需要抓取阅读数"""
class HotWeibo_huati_Grasp():
	def __init__(self):
		self.dr=webdriver.Chrome()
		self.dr.maximize_window()
		self.lg_url="http://weibo.com/"
		self.base_url="http://d.weibo.com/100803?cfs=&Pl_Discover_Pt6Rank__5_filter=hothtlist_type%3D1#_0"
	def by_Name(self,name):
		return self.dr.find_element_by_name(name)
	def by_Xpath(self,xpath):
		return self.dr.find_element_by_xpath(xpath)
	def by_Xpaths(self,xpath):
		return self.dr.find_elements_by_xpath(xpath)
	def login_weibo(self,username,password):
		self.dr.get(self.lg_url)
		time.sleep(3)
		self.by_Name("username").send_keys(username)
		self.by_Name("password").send_keys(password)
		self.by_Xpath("//div[@class='info_list login_btn']/a").click()
		time.sleep(3)
	def grasp(self):
		#调用登录模块
		self.login_weibo("18801340078","wq15803863660")
		self.dr.get(self.base_url)
		list_=self.by_Xpaths("//ul[@class='pt_ul clearfix']//a[@target='_blank']")
		time.sleep(3)
		file_=open("test.txt",'w+')
		read_num=[]
		hot_weibo=[]
		for i in list_:
			if "#" in i.text:
				hot_weibo.append(i.text[1:-1])  #热门微博主题列表
		for i in self.by_Xpaths("//span[@class='number']"):
			read_num.append(i.text) #热门微博主题阅读量
		#写入txt文件
		for i in range(len(hot_weibo)):  
			file_tianchong="\n********************\n"
			file_.write(hot_weibo[i].encode('utf-8'))
			
			file_.write(read_num[i].encode('utf-8'))
			file_.write(file_tianchong)
		self.dr.quit()
			
if __name__ == '__main__':
	weibo=HotWeibo_huati_Grasp()
	weibo.grasp()
