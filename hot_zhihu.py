#coding:utf-8
"""抓取知乎今日最热及本月最热的问题和首个问答，保存至html文件，该html文件的文件名应该是20160228_zhihu_today_hot.html，
也就是日期+zhihu_today_hot.html"""
from selenium import webdriver
import time
class HotZhihu():
	def __init__(self):
		self.dr=webdriver.Chrome()
		self.dr.maximize_window()
		self.month_url="https://www.zhihu.com/explore#monthly-hot"
		self.day_url="https://www.zhihu.com/explore#daily-hot"
	def by_Xpaths(self,xpath):
		return self.dr.find_elements_by_xpath(xpath)
	def grasp_daily(self):
		self.dr.get(self.day_url)
		#问题集定位
		question_elements=self.by_Xpaths("//div[@data-type='daily']//a[@class='question_link']")
		#把所有答案全部展开
		button_elements=self.by_Xpaths("//div[@data-type='daily']//a[@class='toggle-expand']")
		for i in button_elements:
			i.click()
			time.sleep(5)
		questiones_daily=[]
		anwser_daily=[]
		for i in question_elements:
			questiones_daily.append(i.text)
		#所有问答定位
		anwser_elements=self.by_Xpaths("//div[@data-type='daily']//div[@class='zm-item-rich-text expandable js-collapse-body']")
		for i in anwser_elements:
			anwser_daily.append(i.get_attribute('innerHTML'))
		time_now=time.strftime('%Y%m%d')
		#命名文件名
		file_name=time_now+"_zhihu_today_hot.html"
		f1=open(file_name,'w+')
		#写入文件
		for i in range(len(questiones_daily)):
			file_tichong="\n****************************************************\n"
			f1.write(questiones_daily[i].encode('utf-8'))
			f1.write("\n")
			f1.write(anwser_daily[i].encode('utf-8'))
			f1.write(file_tichong)
		f1.close()
		#self.dr.quit()
	#抓取本月热点，与抓取今日热点思路一样
	def grasp_month(self):
		self.dr.get(self.month_url)
		question_elements=self.by_Xpaths("//div[@data-type='monthly']//a[@class='question_link']")
		button_elements=self.by_Xpaths("//div[@data-type='monthly']//a[@class='toggle-expand']")
		for i in button_elements:
			i.click()
			time.sleep(5)
		questiones_daily=[]
		anwser_daily=[]

		for i in question_elements:
			questiones_daily.append(i.text)
		anwser_elements=self.by_Xpaths("//div[@data-type='monthly']//div[@class='zm-item-rich-text expandable js-collapse-body']")
		for i in anwser_elements:
			anwser_daily.append(i.get_attribute('innerHTML'))
		time_now=time.strftime('%Y%m%d')
		file_name=time_now+"_zhihu_month_hot.html"
		f1=open(file_name,'w+')
		for i in range(len(questiones_daily)):
			file_tichong="\n****************************************************\n"
			f1.write(questiones_daily[i].encode('utf-8'))
			f1.write("\n")
			f1.write(anwser_daily[i].encode('utf-8'))
			f1.write(file_tichong)
		f1.close()
		self.dr.quit()
	#把抓取今日热点和抓取本月热点写入一个方法，方便运行
	def grasp_day_month(self):
		self.grasp_daily()
		time.sleep(5)
		self.grasp_month()
if __name__ == '__main__':
	hotzhihu=HotZhihu()
	hotzhihu.grasp_day_month()


