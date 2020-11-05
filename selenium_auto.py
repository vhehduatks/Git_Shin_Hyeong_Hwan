from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By

import time
import os
import datetime
import logging
import traceback


class selenium_auto:

    def __init__(self,USER_ID,USER_PASS,Channel_value,File_path):
        self.login_url='https://center-pf.kakao.com'
        self.channel_url='https://center-pf.kakao.com/profiles'
        self.USER_ID=USER_ID
        self.USER_PASS=USER_PASS
        self.Channel_value=Channel_value
        self.File_path=File_path
        self.driver=webdriver.Chrome()
        self.Nowtime=datetime.datetime.now()
       
        

    def LOGIN(self):

        self.driver.get(self.login_url)
        self.driver.maximize_window()
        action = ActionChains(self.driver)
        self.driver.find_element_by_css_selector('#loginEmailField').click()
        action.send_keys(self.USER_ID).send_keys(Keys.TAB).send_keys(self.USER_PASS).send_keys(Keys.TAB).send_keys(Keys.ENTER).perform()
        time.sleep(1)
        try:    
            print(type(self.driver.find_element_by_id("errorAlert")))
            logging.info(self.Nowtime.strftime(' %Y_%m_%d %H:%M')+":: "+"LOGIN 과정에서 예외상황이 발생하였습니다.")
            self.CLOSE_DRIVER()  
        except NoSuchElementException:
            print("LOGIN pass")
            pass
    
        self.driver.execute_script(
            'window.open("' +
            self.channel_url +
            '");'
        )

        time.sleep(1)
        self.driver.switch_to_window(self.driver.window_handles[0])
        self.driver.close()
        self.driver.switch_to_window(self.driver.window_handles[0]) #return focus    

    
    def SET_CHANNEL(self):
        try:
            Channel=self.driver.find_element_by_xpath("//a[@href='"+self.Channel_value+"']")
            Channel.click()
        except Exception as e:
            logging.info(self.Nowtime.strftime(' %Y_%m_%d %H:%M')+":: "+type(e)+": SET_CHANNEL 과정에서 예외상황이 발생하였습니다.")
            self.CLOSE_DRIVER()
    
    def MAKE_FILE_PATH(self):

        File_list=os.listdir(self.File_path)
        End_of_file=File_list[len(File_list)-1]
        logging.info(self.Nowtime.strftime(' %Y_%m_%d %H:%M')+":: "+End_of_file+ ": 파일이 성공적으로 업로드되었습니다.")
        return os.path.join(self.File_path,End_of_file)

    def SET_POST(self):

        Message=self.Nowtime.strftime('%Y_%m_%d %H:%M')+" 에 작성되었음"
        
        self.driver.get(self.login_url+self.Channel_value+'/posts')
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="mArticle"]/div/div/div[1]/div[2]/form/div/div/div/div/div/textarea').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="mArticle"]/div/div/div[1]/div[2]/form/div/div/div/div/div/textarea').send_keys(Message)#text경로를 제대로 명시할것 div단위로 경로표시할경우 입력안될수있음
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="mArticle"]/div/div/div[1]/div[2]/form/ul/li[1]/div/input').send_keys(self.MAKE_FILE_PATH())
        self.driver.find_element_by_xpath("//*[@id=\"mArticle\"]/div/div/div[1]/div[2]/form/div[4]/div[2]/div[2]/button[2]").click()
        time.sleep(1)

    def GET_SOURCE(self,Num=0):
        try:
            self.driver.get('https://center-pf.kakao.com'+self.Channel_value+'/posts')
            time.sleep(1)
            post=self.driver.find_elements(By.CLASS_NAME,'img_collage')
        except Exception as e:
            print(e) 


        return post[Num].find_element(By.TAG_NAME,'img').get_attribute("src")

    def STOR_SOURCE(self):
        img_path=self.GET_SOURCE()
        with open('test.txt',"w") as f:
            f.write(img_path)

    def Check_File(self,time,Extension):
        
        File_list=os.listdir(self.File_path)
        End_of_file=File_list[len(File_list)-1]
        Temp=self.Nowtime.strftime(time)
        
        if Temp in End_of_file:
            if Extension in End_of_file:
                pass
            else:
                logging.info(self.Nowtime.strftime(' %Y_%m_%d %H:%M')+":: "+End_of_file+" 올바르지 않은 파일 형식입니다.")
                self.CLOSE_DRIVER()
                return 0
        else:
            logging.info(self.Nowtime.strftime(' %Y_%m_%d %H:%M')+" :: "+End_of_file+" 올바르지 않은 날짜입니다.")
            self.CLOSE_DRIVER()
            return 0           

    def CLOSE_DRIVER(self):
        self.driver.quit()
        exit()



if __name__ == "__main__":
    
    logging.basicConfig(filename='./log/POST.log',level=logging.INFO)
    USER_ID = 'kakao ID'
    USER_PASS = 'kakao PASS'     
    Channel_value= 'Channel_value'
    File_Directory_Path=r"Upload date path"
    token='%Y%m%d-%H'#검사하고자 하는 시간의 범위를 작성
    Extension='.jpg'#파일의 확장자 결정

    test=selenium_auto(USER_ID,USER_PASS,Channel_value,File_Directory_Path)
    test.LOGIN()
    test.SET_CHANNEL()
    test.Check_File(token,Extension)
    test.SET_POST()
    test.STOR_SOURCE()
    test.CLOSE_DRIVER()