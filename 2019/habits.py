#!/usr/bin/env python

#virgin pulse website
#Click tips and healthy habits every day.
#Powered by kai.liang
#Created date: 2019-05-16
   
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
    
    
class Option_Virgin():

    def __init__(self,username, passwd, url):
        self.username = username
        self.passwd = passwd
        self.url = url
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(15)
    
    def get_snapshot(self):
        """get screen snapshot"""
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "screenshots")
        if not os.path.exists(path):
            os.mkdir(path)
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = path + "/" + rq + ".png"
        try:
            self.driver.get_screenshot_as_file(screen_name)
            print("save screen shot:%s successully"% screen_name)
        except BaseException:
            print("save screen shot failed")

    def find_element(self, *selector):
        """locate the element"""
        by = selector[0]
        value = selector[1]
        print("try to get element:%s with method:%s"%( value, by))
        element = None
        if by == 'id' or by == 'name' or by == 'class' or by == 'tag' or by == 'link' or by == 'plink' or by == 'css' or by == 'xpath':
            try:
                if by == 'id':
                    element = self.driver.find_element_by_id(value)
                elif by == 'name':
                    element = self.driver.find_element_by_name(value)
                elif by == 'class':
                    element = self.driver.find_element_by_class_name(value)
                elif by == 'tag':
                    element = self.driver.find_element_by_tag_name(value)
                elif by == 'link':
                    element = self.driver.find_element_by_link_text(value)
                elif by == 'plink':
                    element = self.driver.find_element_by_partial_link_text(value)
                elif by == 'css':
                    element = self.driver.find_element_by_css_selector(value)
                elif by == 'xpath':
                    element = self.driver.find_element_by_xpath(value)
                else:
                    print("locate method:%s is wrong" % by)

                return element
            except NoSuchElementException:
                print("catch exception when get element")
                self.get_snapshot()
        else:
            print("can't support the locate method:%s"% by)

    def find_elements(self, *selector):
        """locate list of elements"""
        by = selector[0]
        value = selector[1]
        print("try to get list of elements:%s with method:%s" % (value, by))
        element_l = []
        if by == 'id' or by == 'name' or by == 'class' or by == 'tag' or by == 'link' or by == 'plink' or by == 'css' or by == 'xpath':
            try:
                if by == 'id':
                    element_l = self.driver.find_elements_by_id(value)
                elif by == 'name':
                    element_l = self.driver.find_elements_by_name(value)
                elif by == 'class':
                    element_l = self.driver.find_elements_by_class_name(value)
                elif by == 'tag':
                    element_l = self.driver.find_elements_by_tag_name(value)
                elif by == 'link':
                    element_l = self.driver.find_elements_by_link_text(value)
                elif by == 'plink':
                    element_l = self.driver.find_elements_by_partial_link_text(value)
                elif by == 'css':
                    element_l = self.driver.find_elements_by_css_selector(value)
                elif by == 'xpath':
                    element_l = self.driver.find_elements_by_xpath(value)
                else:
                    print("locate method:%s is wrong", by)
    
                return element_l
            except NoSuchElementException:
                print("catch exception when get element")
                self.get_snapshot()
        else:
            print("can't support the locate method:%s"% by)
    
    def click(self, selector):
            """click the element"""
            element = self.find_element(selector)
            try:
                element.click()
                logger.info("click the element successfully")
            except BaseException:
                logger.error("catch exception when click the element", exc_info=1)
                self.get_snapshot()
   
    def got_it(self):
        gotit0 = self.find_element("id", "triggerCloseCurtain")
        if gotit0:
            gotit0.click()
            time.sleep(2)
        gotit1 = self.find_element( "id", "triggerCloseCurtain")
        if gotit1:
            gotit1.click()
            time.sleep(3)

    def healthy(self):
        healthy_btn = self.find_element( "id", "nav-tracking-menu")
        if healthy_btn:
            healthy_btn.click()
        
        self.find_element( "id", "tracker-49-track-yes").click()
        time.sleep(1)
        self.find_element( "id", "tracker-626-track-yes").click()
        time.sleep(1)
        self.find_element( "id", "tracker-627-track-yes").click()
        time.sleep(1)
        self.find_element( "id", "tracker-62-track-yes").click()
        time.sleep(1)
        self.find_element( "id", "tracker-692-track-yes").click()
        
        print("Tracking habits sucessfully!") 
        #ActionChains(self.driver).move_to_element(home_btn).perform()

    def main(self):

        #in_username = driver.find_element_by_id('username')
        in_username = self.find_element( "id", "username")
        if in_username:
            in_username.clear()
            in_username.send_keys(self.username)
        else:
            return "Cannot find username input"
    
        #in_passwd = driver.find_element_by_id('password')
        in_passwd = self.find_element( "id", "password")
        in_passwd.clear()
        in_passwd.send_keys(self.passwd) 
        
        login = self.find_element( "id", "kc-login")
        #tmp = login
        #print("login")
        #print(tmp)
        #print(dir(tmp))
        login.click()
        time.sleep(10)
        modal_win = self.find_element( "id", "trophy-modal-close-btn")
        if modal_win:
            modal_win[0].click()
            time.sleep(3)
        time.sleep(2)
         
        self.got_it()
        healthy_btn = self.find_element( "id", "nav-tracking-menu")
        #healthy_btn = self.find_element( "class", "rewards-btn-container")
        if healthy_btn:
            healthy_btn.click()
            time.sleep(2)
            self.healthy()
    
    
        #self.driver.quit()
    
    
    
if __name__ == "__main__":
    username = "email.com"
    passwd = "password"
    url = "https://member.virginpulse.com/login.aspx"
    habits = Option_Virgin(username, passwd,url)
    habits.main()
    
    
    
