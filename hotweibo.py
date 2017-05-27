#coding:utf-8
"""抓取24小时热门微博前十条(http://d.weibo.com/102803?from=unlogin_home&mod=pindao&type=hotweibo#_rnd1456632403002)
保存成txt格式，需要抓取发帖人，正文的html，转发量，评论数和赞的数量"""
from selenium import webdriver
import time
class HotWeibo_Grasp(object):
	def __init__(self):
		self.dr=webdriver.Chrome()
		self.dr.maximize_window()
		self.weibo_url="http://weibo.com/"
		self.base_url="http://d.weibo.com/102803?from=unlogin_home&mod=pindao&type=hotweibo#_rnd1456632403002"
	def by_Name(self,name):
		return self.dr.find_element_by_name(name)
	def by_Xpath(self,xpath):
		return self.dr.find_element_by_xpath(xpath)
	def by_Xpaths(self,xpath):
		return self.dr.find_elements_by_xpath(xpath)
	def login_weibo(self,username,password):
		self.dr.get(self.weibo_url)
		time.sleep(3)
		self.by_Name("username").send_keys(username)
		self.by_Name("password").send_keys(password)
		self.by_Xpath("//div[@class='info_list login_btn']/a").click()
		time.sleep(3)
	def grasp(self):
		#调用登录模块
		self.login_weibo("18801340078","wq15803863660")
		self.dr.get(self.base_url)
		time.sleep(3)
		elements_user=self.by_Xpaths("//*[@id='Pl_Core_NewMixFeed__3']/div/div[3]//div[@class='WB_info']")
		elements_text=self.by_Xpaths("//*[@id='Pl_Core_NewMixFeed__3']/div/div[3]//div[@class='WB_text W_f14']")
		elements_send=self.by_Xpaths("//*[@id='Pl_Core_NewMixFeed__3']/div/div[3]//ul[@class='WB_row_line WB_row_r4 clearfix S_line2']/li[2]")
		elements_discuss=self.by_Xpaths("//*[@id='Pl_Core_NewMixFeed__3']/div/div[3]//ul[@class='WB_row_line WB_row_r4 clearfix S_line2']/li[3]")
		elements_praise=self.by_Xpaths("//*[@id='Pl_Core_NewMixFeed__3']/div/div[3]//ul[@class='WB_row_line WB_row_r4 clearfix S_line2']/li[4]")
		time.sleep(3)
		#截取前10发帖人
		username_elements=elements_user[0:10]
		#截取前十发帖人正文
		text_elements=elements_text[0:10]
		#截取前十微博的转发量
		send_elements=elements_send[0:10]
		#截取前十微博的评论数
		discuss_elements=elements_discuss[0:10]
		#截取前十微博的点赞数
		praise_elements=elements_praise[0:10]
		#发帖人
		usernames=[]
		#微博正文
		texts=[]
		#转发数
		forwards=[]
		#评论数
		discusses=[]
		#点赞数
		praises=[]
		#把发帖人写入列表
		for i in username_elements:
			usernames.append(i.text)
		#把发布正文写入列表
		for i in text_elements:
			texts.append(i.text)
		#把前十微博的转发量写入列表
		for i in send_elements:
			forwards.append(i.text)
		#把前十微博的评论数写入列表
		for i in discuss_elements:
			discusses.append(i.text)
			
		#把把前十微博的点赞数写入列表
		for i in praise_elements:
			praises.append(i.text[1:])
		#写入txt文件
		f1=open("test.txt",'w+')
		for i in range(len(username_elements)):
			file_tianchong="\n*****************************************************\n"
			f1.write("发帖人："+usernames[i].encode('utf-8')+".")
			f1.write("微博正文："+texts[i].encode('utf-8')+".")
			f1.write("转发数："+forwards[i].encode('utf-8')+".")
			f1.write("评论数："+discusses[i].encode('utf-8')+".")
			f1.write("点赞数："+praises[i].encode('utf-8')+".")

			f1.write(file_tianchong)
		f1.close()
		self.dr.quit()

if __name__ == '__main__':
	hot=HotWeibo_Grasp()
	hot.grasp()

