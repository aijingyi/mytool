#!/usr/bin/python
#coding:utf-8
import urllib2
import re
import os

#查看quips所使用的网址
url = "http://192.168.32.3/buglist.cgi?query_format=advanced&list_id=81057&short_desc=123&short_desc_type=allwordssubstr&product=smb_DEV"

def getquip():
	html = urllib2.urlopen(url).read()  #读取网页内容
	rules = r'"quips.cgi"><i>(.*)</i></a>'
	reg = re.compile(rules)
	quip = re.findall(reg,html)         #使用正则表达式提取quips字符
	quip = ''.join(quip) 
	#print quip
	q = open('quips.txt', 'r+')
	quips = q.read()
	q.close()                               #读取文件内容
	if quip not in quips:                   #如果获取的quip不在quips.txt文件里则写入文件
		f = open('quips.txt', 'a')
		f.write(quip)
		f.write('\n')
		f.close()
def isquips():
	if not os.path.isfile('quips.txt'):
		a = os.system('touch quips.txt')    #判断quips.txt是否存在，不存在就创建
if __name__ == "__main__":
	print "Getting quips, please waiting....."	
	isquips()
	for i in range(100):    #获取100个quips
		getquip()
	print "Getting quips completed, please look over the quips.txt."
