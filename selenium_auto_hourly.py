from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *

import time
import os
import datetime
import logging
import traceback

logging.basicConfig(filename='./log/POST.log',level=logging.INFO)
driver = webdriver.Chrome()
login_url = 'https://center-pf.kakao.com/'
channel_url = 'https://center-pf.kakao.com/profiles'
driver.get(login_url)
driver.maximize_window()
action = ActionChains(driver)
USER_ID = 'kakao ID'
USER_PASS = 'kakao PASS'     
Channel_value01= 'Channel_value'
Autoit_Path=r"FileUpload.exe path"
File_Directory_Path=r"Upload date path"
Nowtime=datetime.datetime.now()



def LOGIN(ID, PASS):
    
    driver.find_element_by_css_selector('#loginEmailField').click()
    action.send_keys(ID).send_keys(Keys.TAB).send_keys(PASS).send_keys(Keys.TAB).send_keys(Keys.ENTER).perform()
    time.sleep(1)
    try:    
        print(type(driver.find_element_by_id("errorAlert")))
        logging.info(Nowtime.strftime(' %Y_%m_%d %H:%M')+":: "+"LOGIN 과정에서 예외상황이 발생하였습니다.")
        CLOSE_DRIVER()  
    except NoSuchElementException:
        print("LOGIN pass")
        pass
 
 

    driver.execute_script(
        'window.open("' +
        channel_url +
        '");'
    )

    time.sleep(1)
    driver.switch_to_window(driver.window_handles[0])
    driver.close()
    driver.switch_to_window(driver.window_handles[0]) #return focus

def SET_CHANNEL(Channel_value):
    try:
        Channel=driver.find_element_by_xpath("//a[@href='"+Channel_value+"']")
        Channel.click()
    except Exception as e:
        logging.info(Nowtime.strftime(' %Y_%m_%d %H:%M')+":: "+type(e)+": SET_CHANNEL 과정에서 예외상황이 발생하였습니다.")
        CLOSE_DRIVER()


def SET_POST():

    Message=Nowtime.strftime('%Y_%m_%d %H:%M')+" 에 작성되었음"

    time.sleep(1)
    driver.find_element_by_xpath("//*[@id=\"kakaoGnb\"]/div/div/ul[4]/li[1]/a").click()    
    time.sleep(1)
    Check_File()
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id=\"mArticle\"]/div/div/div[1]/div[2]/form/ul/li[1]/div").click()  
    time.sleep(2)
    RUN_AUTOIT()
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id=\"mArticle\"]/div/div/div[1]/div[2]/form/div[2]/div/div/div/div/textarea").send_keys(Message)#text경로를 제대로 명시할것 div단위로 경로표시할경우 입력안될수있음
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id=\"mArticle\"]/div/div/div[1]/div[2]/form/div[4]/div[2]/div[2]/button[2]").click()
    time.sleep(1)


def RUN_AUTOIT():

    Autoit_File_Path=MAKE_FILE_PATH()
    time.sleep(1)
    os.system(Autoit_File_Path)

def MAKE_FILE_PATH():

    File_list=os.listdir(File_Directory_Path)
    End_of_file=File_list[len(File_list)-1]
    logging.info(Nowtime.strftime(' %Y_%m_%d %H:%M')+":: "+End_of_file+ ": 파일이 성공적으로 업로드되었습니다.")
    return Autoit_Path +" \""+File_Directory_Path +"\\"+ End_of_file + "\""
   


def Check_File():

    File_list=os.listdir(File_Directory_Path)
    End_of_file=File_list[len(File_list)-1]
    #hourly 형식 Hourly_Temp_YYYY_MM_DD_HH.png 이므로 시간별로 체크
    Temp=Nowtime.strftime('%Y%m%d-%H')
    Extension=".png"
    if Temp in End_of_file:
        if Extension in End_of_file:
            pass
        else:
            logging.info(Nowtime.strftime(' %Y_%m_%d %H:%M')+":: "+End_of_file+" 올바르지 않은 파일 형식입니다.")
            CLOSE_DRIVER()
            return 0
    else:
        logging.info(Nowtime.strftime(' %Y_%m_%d %H:%M')+" :: "+End_of_file+" 올바르지 않은 날짜입니다.")
        CLOSE_DRIVER()
        return 0           

def SEND_MESSAGE():

    Message=Nowtime.strftime('%Y_%m_%d %H:%M')+" 에 작성되었음"

    time.sleep(1)
    driver.find_element_by_xpath("//*[@id=\"kakaoGnb\"]/div/div/ul[3]/li[1]/a/span[1]").click()    
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id=\"mArticle\"]/div[2]/ul/li[1]/button").click()
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id=\"messageWrite\"]").send_keys(Message)
    time.sleep(1)
    # action.send_keys("Message").perform() //ElementNotInteractableException 발생할경우엔 click사용해야할수 있음
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id=\"mArticle\"]/div/form/div[2]/span/div/button[2]").click()
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id=\"mArticle\"]/div/form/div[2]/button[4]").click()
    time.sleep(1)
    try:
        Alert=driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[2]/strong").text     
        print(Alert)
    except NoSuchElementException as e:
        KeyToken="메시지 발송이 바로 시작됩니다."
        Alert=driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div/strong").text
        print(type(e),": "+Alert)
        if(Alert==KeyToken):
            driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div/div[2]/button[2]").click()
    except Exception as e:
        logging.info(Nowtime.strftime(' %Y_%m_%d %H:%M')+":: "+type(e)+": SEND_MESSAGE 과정에서 예외상황이 발생하였습니다.")
        CLOSE_DRIVER()



def CLOSE_DRIVER():
    driver.quit()
    exit()

    

LOGIN(USER_ID,USER_PASS)
SET_CHANNEL(Channel_value01)
SET_POST()
CLOSE_DRIVER()
