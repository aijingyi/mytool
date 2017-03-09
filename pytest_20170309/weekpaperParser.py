#!/usr/bin/python
#coding:utf-8

####################
#本文档爬取周报系统所有同事的最近一篇周报
#powered by: kai.liang@i-soft.com.cn
#date:20170224
#version:1.0
######################

import urllib,urllib2
import re                  #载入所需模块


class Bloglist():
    url='http://tfs.i-soft.com.cn/drupal/?q=blog/'  #周报系统日志网址的前缀

    def __init__(self, userid):
        self.url=Bloglist.url+str(userid)          #网址=网址前缀+用户id
    def getHtml(self):                             #获取网页内容
        try:
            html = urllib2.urlopen(self.url).read()
            return html
        except Exception, e:
            print 'url error!!'


    def getTitle(self):                          #应用正则表达式提取网页中的日志标题
	html=self.getHtml()
        reg = r'node/\d+">(.*\d{6}.*)</a></h1>'
        titlere = re.compile(reg)
        lines = html.split()
        m = re.search(titlere, html)
        titles = m.groups()
        title = ''.join(titles)
        return title
def main():
    """
    zhaopanpan:7
    lixiaoshuang:21
    huangjun:22
    wangjue:23
    liuke:24
    lipeng:28
    hanjingjing:30
    lixingfeng:41
    liuhui:42
    liangkai:43
    liulu:44
    zhaolili:45
    yaoxiangchuang:46
    liuchang:47
    liuchunyuan:48
    lufei:49
    liuyang:50
    chijianping:51
    
    """                  #每位用户的id
    users = [7,21,22,23,24,28,30,41,42,43,44,45,46,47,48,49,50,51]
    print '----------------------------'
    print '测试中心成员最近一篇周报'
    print '----------------------------'
    for i in users:
        userBlog = Bloglist(i)         #对象初始化
        title = userBlog.getTitle()    #使用对象方法
        print title  
    print '----------------------------'
  

if __name__== '__main__':
    main()
