#coding:utf-8
"""抓取豆瓣读书中的(http://book.douban.com/)最受关注图书，
按照评分排序，并保存至txt文件中，需要抓取书籍的名称，作者，评分，体裁和一句话评论
"""
from selenium import webdriver
import time
class DouB_Book(object):
	def __init__(self):
		self.dr=webdriver.Chrome()
		self.dr.maximize_window()
		self.url="http://book.douban.com/"
	def by_Xpaths(self,xpath):
		return self.dr.find_elements_by_xpath(xpath)
	def by_Xpath(elf,xpath):
		return self.dr.find_element_by_xpath(xpath)
	def grasp(self):
		def by_score(dic):
			return float(dic['score'])
		self.dr.get(self.url)
		time.sleep(3)
		ares=self.by_Xpaths("//*[@id='content']/div/div[1]/div[3]/div[2]/ul//li")
		
		books=[]
		for i in ares:
			item={}
			#print i.find_element_by_css_selector('h4.title').text
			#print i.text
			#print i.find_element_by_xpath("//p[@class='author']").text
			#print i.find_element_by_css_selector('p.author').text
			
			item['title']=i.find_element_by_css_selector('h4.title').text
			item['author']=i.find_element_by_css_selector('p.author').text
			item['score']=i.find_element_by_css_selector('span.average-rating').text
			item['types']=i.find_element_by_css_selector('p.book-list-classification').text
			item['comment']=i.find_element_by_css_selector('p.reviews').text
			books.append(item)

		books_group_by_score=sorted(books,key=by_score,reverse=True)
		time_now=time.strftime('%H-%M-%S')
		filename=time_now+"douban_book.txt"
		f1=open(filename,'w+')
		for book in books_group_by_score:
			file_tianchong="\n***********************************************\n"
			f1.write("书名:"+book['otitle'].encode('utf-8')+",")
			f1.write("作者："+book['author'].encode('utf-8')+",")
			f1.write("评分："+book['score'].encode('utf-8')+",")
			f1.write("类型："+book['types'].encode('utf-8')+",")
			f1.write("评论："+book['comment'].encode('utf-8')+".")
			f1.write(file_tianchong)
			
		
		self.dr.quit()
if __name__ == '__main__':
	db=DouB_Book()
	db.grasp()
