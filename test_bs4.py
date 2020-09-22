from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from flask import request
from flask import Flask
from flask import jsonify


import requests
import time
import os
import datetime
import logging
import traceback

logging.basicConfig(filename='./log/POST.log',level=logging.INFO)
login_url = 'https://center-pf.kakao.com/'
channel_url = 'https://center-pf.kakao.com/profiles'
USER_ID = 'hegyna1@naver.com'
USER_PASS = 'gudghks20!'     
Channel_value01= '/_xcKxebxb'
Channel_value02= '/_lxhxgxdK'
Nowtime=datetime.datetime.now()

selenium_option=webdriver.ChromeOptions()
selenium_option.add_argument('headless')
selenium_option.add_argument('disable-gpu')
selenium_option.add_argument('lang=ko_KR')
#driver = webdriver.Chrome(options=selenium_option)
driver = webdriver.Chrome()
action = ActionChains(driver)


def LOGIN(ID, PASS):
    
    driver.get(login_url)
    driver.find_element(By.ID,'loginEmailField').click()

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

Token=''

def GET_SOURCE(Channel_value,Num=0,Token="default"):
    
    if Token=="default":
        driver.get('https://center-pf.kakao.com'+Channel_value+'/posts')
        time.sleep(1)
        post=driver.find_elements(By.CLASS_NAME,'img_collage')
    else:
        try:
            driver.get('https://center-pf.kakao.com'+Channel_value+'/posts')
            time.sleep(1)
            for p in post:
                print("img src : "+p.find_element(By.TAG_NAME,'img').get_attribute("src"))
        except Exception as e:
            print(e)
       

    # for p in post:
       
    #    print("img src : "+p.find_element(By.TAG_NAME,'img').get_attribute("src"))

    return post[Num].find_element(By.TAG_NAME,'img').get_attribute("src")

def GET_Link(file_name):
    try:
        with open(file_name,'r') as f:
            img_link=f.read()

        return img_link    
    except Exception as e:
            print(e)



def CLOSE_DRIVER():
    driver.quit()
    exit()



LOGIN(USER_ID,USER_PASS)
#SET_CHANNEL(Channel_value01)
print(GET_SOURCE(Channel_value02))




# def API_SKILL():

 
req=requests.get('https://center-pf.kakao.com/_xcKxebxb/posts')
html=req.text
soup=BeautifulSoup(html,'html.parser')

print(soup)
print(type(soup))


app=Flask(__name__)


@app.route('/')
def testmain():
    return "Hello_world"

@app.route('/testskill01',methods=['POST'])

def func01():
    
    driver.refresh()
    time.sleep(1)
    content = request.get_json()
    content = content['userRequest']
    Client_Message = content['utterance']
    print(Client_Message)
    res={   
        "version": "2.0",
        "template": 
        {
            "outputs": 
            [
                {
                    "simpleImage": 
                    {
                        "imageUrl": GET_Link('CCTV.txt'),
                        "altText": "1번 채널 사진입니다."
                    }
                }
            ]
        }
    }
    return jsonify(res)

@app.route('/testskill02',methods=['POST'])

def func02():
    
    driver.refresh()
    time.sleep(1)
    content = request.get_json()
    content = content['userRequest']
    Client_Message = content['utterance']
    print(Client_Message)
    res={   
        "version": "2.0",
        "template": 
        {
            "outputs": 
            [
                {
                    "simpleImage": 
                    {
                        "imageUrl": GET_Link('Hourly.txt'),
                        "altText": "2번 채널 사진입니다."
                    }
                }
            ]
        }
    }
    return jsonify(res)

@app.route('/testskill03',methods=['POST'])

def func03():
    
    driver.refresh()
    time.sleep(1)
    content = request.get_json()
    content = content['userRequest']
    Client_Message = content['utterance']
    print(Client_Message)
    res={   
        "version": "2.0",
        "template": 
        {
            "outputs": 
            [
                {
                    "simpleImage": 
                    {
                        "imageUrl": GET_Link('daily.txt'),
                        "altText": "18시 30분 현장 사진입니다."
                    }
                }
            ]
        }
    }
    return jsonify(res)


if __name__=="__main__":
    app.run(host='0.0.0.0',port='8080')

# 168.131.70.215
#노트북 168.131.70.50