#!/usr/bin/python
#coding:utf-8

##################
#爬取测试技术分享里指定某一月所有同事的文章发布数量
#powered by: kai.liang@i-soft.com.cn
#date: 20170307
#version: 1.0
#################

import urllib2
import re
import sys    #载入网络、正则、系统的模块

try:
    month = sys.argv[1]      #运行脚本时传递的参数
except Exception as e:
    print '请输入参数，例如：'
    print '查询3月份的文章请输入：python blog-spider.py 03'
    exit() 
year = 2017                 #默认年份为2017，可以此处修改

class Bloglist():           #定义类，脚本的核心
    total_zhuan=0
    total_yuan=0
    total = 0
    urlHead = 'http://192.168.32.3/blog/?author=%s&&m=%s'
    def __init__(self, author, date='201703'):        #初始化参数
        self.url = self.urlHead %(author,date)
        self.zhuan = 0
        self.yuan = 0
    def getHtml(self):                             #获取网页文本
        html = urllib2.urlopen(self.url).read()
        return html
    def getTitle(self):                            #获取网页中某一作者的文章标题
        reg = r'"bookmark">(.*)</a></h2>'
        titlere = re.compile(reg)
        title = re.findall(titlere, self.getHtml())
        return title
    def count(self):                  #计算作者的文章数量，本打算输出文章标题
                                      #看着乱，就给注释掉了
	#print "文章标题："
	#print "-----------------------------"
        for line in self.getTitle():
	    if not line.startswith("<time") and not line.startswith("<img"): 
           # if '转载' or '（转）' in line:
                if '转载' in line or line[0:9]== '（转）':
                    self.zhuan += 1
                else:
                    self.yuan += 1
                #print line
	#print "-----------------------------"
	print "发布文章：" + str(self.zhuan+self.yuan) + "篇 ",
	print "转载："+ str(self.zhuan) + "篇 " + "原创：" + str(self.yuan) + "篇"
	Bloglist.total_zhuan = Bloglist.total_zhuan + self.zhuan
	Bloglist.total_yuan = Bloglist.total_yuan + self.yuan
	Bloglist.total = Bloglist.total_zhuan + Bloglist.total_yuan
def author():
    date = str(year) + str(month)
    user = { 5:'黄  俊', 7:'李小双', 8:'赵盼盼', \
10:'刘  珂',11:'刘  辉', 12:'刘春媛', 13:'路  斐', 14:'梁  凯', 15:'李兴峰', 16:'刘  璐',\
 17:'姚翔川',18:'刘  畅', 19:'刘  杨', 20:'赵丽丽', 21:'迟建平'}
    #测试成员对应的id
    print "-------------------------------------------"
    print "2017年%s月份测试中心成员发布文章情况" %month
    print "-------------------------------------------"
    for i in user.keys():
        userPaper = Bloglist(i, date)     #成员对象的实例化
        print '%s' %user[i],
        userPaper.count()
    print "总计：%s篇，转载：%s篇，原创：%s篇" %(Bloglist.total, Bloglist.total_zhuan, Bloglist.total_yuan)
    print "-------------------------------------------"
    
if __name__ == '__main__':
    author()
