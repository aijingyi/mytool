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
import logging
import sys
from pyvirtualdisplay import Display

    

username = "kai.liang@windriver.com"
passwd = "password"
url = "https://member.virginpulse.com/login.aspx"

if len(sys.argv) > 1:
    debug = 1
else:
    debug = 0


logging.basicConfig(filename=os.path.join('/tmp/', 'virgin-habits.log'),
                    format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]',
                    level = logging.INFO,
                    filemode='a',
                    datefmt='%Y-%m-%d-%I:%M:%S %p')

logger = logging.getLogger(__name__)
    
class Option_Virgin():

    def __init__(self,username, passwd, url):
        self.username = username
        self.passwd = passwd
        self.url = url
        if debug == 1:
            self.driver = webdriver.Chrome()
        else:
            self.driver = webdriver.Firefox()
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(25)
    
    def get_snapshot(self):
        """get screen snapshot"""
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "screenshots")
        if not os.path.exists(path):
            os.mkdir(path)
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = path + "/" + rq + ".png"
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("save screen shot:%s successully", screen_name)
        except BaseException:
            logger.error("save screen shot failed", exc_info=1)

    def find_element(self, selector):
        """locate the element"""
        by = selector[0]
        value = selector[1]
        logger.info("try to get element:%s with method:%s", value, by)
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
                    logger.error("locate method:%s is wrong" , by, exc_info=1)

                return element
            except NoSuchElementException:
                logger.error("catch exception when get element" )
                #self.get_snapshot()
        else:
            logger.error("can't support the locate method:%s", by, exc_info=1)

    def find_elements(self, selector):
        """locate list of elements"""
        by = selector[0]
        value = selector[1]
        logger.info("try to get list of elements:%s with method:%s"  ,value, by)
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
                    logger.info("locate method:%s is wrong", by)
    
                return element_l
            except NoSuchElementException:
                logger.error("catch exception when get element")
                #self.get_snapshot()
        else:
            logger.error("can't support the locate method:%s", by, exc_info=1)
    
    def click(self, selector):
            """click the element"""
            element = self.find_element(selector)
            try:
                element.click()
                logger.info("click the element successfully")
            except BaseException:
                logger.error("catch exception when click the element")
                #self.get_snapshot()

    def input(self, selector, input_value):
        """input the content on element"""
        element = self.find_element(selector)
        element.clear()
        logger.info("clear the input")
        try:
            element.send_keys(input_value)
            #logger.info("input content：%s", input_value)
        except BaseException:
            logger.error("catch exception when input the content")
            #self.get_snapshot()

    def moveto(self, selector):
        """move the mouse to element"""
        element = self.find_element(selector)
        try:
            webdriver.ActionChains(self.driver).move_to_element(element).perform()
            logger.info("move to the element successfully")
        except BaseException:
            logger.error("catch exception when move to the element", exc_info=1)
            #self.get_snapshot()


    def move_and_click(self, selector):
        """move the mouse to element and click it"""
        element = self.find_element(selector)
        try:
            webdriver.ActionChains(self.driver).move_to_element(element).click().perform()
            logger.info("move to and click the element successfully")
        except BaseException:
            logger.error("catch exception when move and click the element", exc_info=1)
            #self.get_snapshot()


    def get_current_window(self):
        """get current window of driver"""
        return self.driver.current_window_handle


    def switch_to_latest_window(self):
        """switch window handler to the latest window"""
        all_handles = self.driver.window_handles
        new_window = all_handles[-1]
        try:
            self.driver.switch_to_window(new_window)
        except BaseException:
            logger.error("switch to latest window failed", exc_info=1)
            #self.get_snapshot()


    def switch_to_target_window(self, target_handle):
        """switch driver's window handler as target one"""
        try:
            self.driver.switch_to_window(target_handle)
        except BaseException:
            logger.error("switch to target window failed", exc_info=1)
            #self.get_snapshot()


    def get_title(self):
        """get page title"""
        title = self.driver.title
        logger.info("the title of current page is:%s", title)
        return title


    def refresh(self):
        """refresh the page"""
        try:
            self.driver.refresh()
            logger.info("refresh successful")
        except BaseException:
            logger.error("refresh failed", exc_info=1)
            #self.get_snapshot()


    def execute_script(self, command, element):
        """execute script command"""
        try:
            self.driver.execute_script(command, element)
            logger.info("success to execute script:%s", command)
        except BaseException:
            logger.error("failed to execute script:%s", command, exc_info=1)
            #self.get_snapshot()

    def quit(self):
        self.driver.quit()  

    def got_cards(self):
        happy_pursuit = self.click(["id", "trophy-modal-close-btn"])
        ture_or_false = self.click(["class", "quiz-true-false-buttons"])
        ture_or_false_1 = self.click(["class", "quiz-true-false-buttons ng-scope"])
        ture_got = self.click(["class", "got-it-core-button"])
   
        time.sleep(1)
        gotit0 = self.click(["id", "triggerCloseCurtain"])
        time.sleep(2)
        gotit1 = self.click( ["id", "triggerCloseCurtain"])

    def track_habits(self):
        healthy_btn = self.click( ["id", "nav-tracking-menu"])
        
        logger.info("track be orgnize.")
        #self.click(["id", "tracker-49-track-yes"])
        time.sleep(1)
        logger.info("track moring drink.")
        #self.click(["id", "tracker-652-track-yes"])
        #time.sleep(1)
        self.click(["id", "tracker-678-track-yes"])
        #time.sleep(2)
        self.click(["id", "tracker-652-track-yes"])
        #time.sleep(2)
        self.click(["id", "tracker-626-track-yes"])
        #time.sleep(2)
        self.click(["id", "tracker-13-track-yes"])
        #time.sleep(2)
        self.click(["id", "tracker-62-track-yes"])
        time.sleep(2)
        self.click(["id", "tracker-692-track-yes"])
        time.sleep(2)
        self.click(["id", "tracker-688-track-yes"])
        time.sleep(2)
        self.click(["id", "tracker-683-track-yes"])
        time.sleep(2)
        self.click(["class", "mood-button ng-scope"])
        logger.info("track staires.")
        self.click(["id", "tracker-13-track-no"])
        
        logger.info("Tracking habits sucessfully!") 

    def main(self):

        #input username and password
        in_username = self.input( ["id", "username"],self.username)
        in_passwd = self.input( ["id", "password"],self.passwd)
        
        #login website
        login = self.click([ "id", "kc-login"])
        time.sleep(15)

        #close 7000 steps and 1000 steps
        modal_win = self.click([ "id", "trophy-modal-close-btn"])
        time.sleep(2)
         
        #got it from cards
        self.got_cards()
        #track healthy habits
        self.track_habits()
 
        #close brower
        self.quit()
    
    
    
if __name__ == "__main__":
    if debug == 0:
        display = Display(visible=0, size=(800, 800))
        display.start()
    habits = Option_Virgin(username, passwd,url)
    habits.main()
