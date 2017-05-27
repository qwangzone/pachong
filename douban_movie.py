#coding:utf-8
"""抓取豆瓣电影(https://movie.douban.com/nowplaying/beijing/)中的正在热映前12部电影，并按照评分排序，保存至txt文件"""
from selenium import webdriver
import time
from operator import itemgetter
import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
class DbMovie():
	def __init__(self):
		self.dr=webdriver.Chrome()
		self.dr.maximize_window()
		self.url="https://movie.douban.com/nowplaying/beijing/"
	def by_Xpaths(self,xpath):
		return self.dr.find_elements_by_xpath(xpath)
	def grasp(self):
		self.dr.get(self.url)
		#定位电影名字与评分位置
		movie_elemenets=self.by_Xpaths("//div[@id='nowplaying']/div[2]//li[@class='list-item']")
		movie_names=[]
		movie_scores=[]
		
		for i in movie_elemenets:
			movie_names.append(i.get_attribute('data-title'))
			print i
		for i in movie_elemenets:
			movie_scores.append(str(i.get_attribute('data-score')))

		movies=zip(movie_names,movie_scores)
		group_by_score=sorted(movies,key=lambda x:x[1], reverse=True)
		f1=open("movies_douban.txt",'w+')
		f1.write("豆瓣热映电影排名：（按分数排名）\n")
		f1.write("\n")
		now_time=time.strftime('%Y-%m-%d %H:%M:%S')
		f1.write(now_time)
		f1.write("\n")
		for i in group_by_score:
			"""
			#另一种写法
			f1.write("电影名字: "+i[0].encode('utf-8')+"电影评分: "+i[1].encode('utf-8'))
			f1.write("\n")
			"""
			f1.write("\n")
			for j in i:
				#f1.write("电影：")
				f1.write(j.encode('utf-8'))
				f1.write("")
				

		#f1.write(group_by_score)
		#f1.close()
		self.dr.quit()
		
		
                                               

if __name__ == '__main__':
	db=DbMovie()
	db.grasp()
