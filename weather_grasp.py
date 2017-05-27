#coding:utf-8
from selenium import webdriver
import time
class WeatherGrasp(object):
	def __init__(self,city):
		self.city=city
		self.base_url="http://www.baidu.com"
		self.dr=webdriver.Chrome()
		self.dr.maximize_window()
		self.wea,self.high_tem,self.low_tem=self.get_tem_wea()
	def by_Xpath(self,path):
		return self.dr.find_element_by_xpath(path)
	def by_Id(self,id):
		return self.dr.find_element_by_id(id)
	def get_tem_wea(self):
		self.dr.get(self.base_url)
		self.by_Id("kw").send_keys(self.city+u"天气")
		time.sleep(3)
		weather=self.by_Xpath("//*[@id='1']/div[1]/div[1]/a[2]/p[4]").text
		time.sleep(3)
		temperature=self.by_Xpath("//*[@id='1']/div[1]/div[1]/a[2]/p[3]").text
		temp_list = temperature.split('~')
		high_temp = int(temp_list[0])
		low_temp=int(temp_list[-1][0:-1])
		return (weather,high_temp,low_temp)
	def send_mail(self):
		print u"明日天气情况为"+self.wea
		print u"最高温度"+str(self.high_tem)
		print u"最低温度"+str(self.low_tem)

		if u"雨" in self.wea:
			print u"明天有雨，请注意带伞"
		elif self.high_tem>30:
			print u"明天高温，请注意防范"
		elif self.low_tem<10:
			print u"明天降温，请注意加衣"
		
		self.dr.quit()
		
if __name__ == '__main__':
	we=WeatherGrasp(u"北京")
	we.send_mail()


