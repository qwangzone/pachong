#coding:utf-8
"""从http://www.pm25.com/shenzhen.html抓取北京，深圳，上海，广州的pm2.5指数，并按照空气质量从优到差排序，保存在txt文档里"""
#import BSTestRunner
from selenium import webdriver
import unittest
import time
class PM25(unittest.TestCase):
    def setUp(self):
        self.dr=webdriver.Chrome()
        self.dr.maximize_window()
        self.url="http://www.pm25.com/"
    def test_get_pm(self):
        cities=["beijing","shenzhen","shanghai","guangzhou"]
        city=[u"北京",u"深圳",u"上海",u"广州"]
        pm=[]
        for i in range(len(cities)):
            self.dr.get(self.url+cities[i]+".html")
            time.sleep(3)
            pm.append(self.dr.find_element_by_css_selector("span.pm25_span").text)
        city_pm=zip(city,pm)
        city_pm_sort=sorted(city_pm,key=lambda x:x[1])
        now_time=time.strftime('%H_%M_%S')
        filename=now_time+"PM.txt"
        f1=open(filename,'w+')
        for i in city_pm_sort:
            f1.write(i[0].encode('utf-8')+":")
            f1.write(i[1])
            f1.write("\n***************************\n")
    def tearDown(self):
        self.dr.quit()
if __name__ == '__main__':
    suit=unittest.TestSuite()
    suit.addTest(PM25('test_get_pm'))
    runner=unittest.TextTestRunner()
    runner.run(suit)
