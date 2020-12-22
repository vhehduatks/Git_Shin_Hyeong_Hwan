import os
import time
# 4324 4347
def make_string(num):
    num=str(num)
    command='ffmpeg.exe -i "'
    base_url='http://mvod.jnu.ac.kr:1935/vod/MP4/yearlyFolder/2020/05/MP4/'
    url='mp4:MP4-'+num+'.mp4/master.m3u8"'
    after=' -bsf:a aac_adtstoasc -c copy'
    filename=" 영상처리"+num+'.mp4'

    
    
    return command+base_url+url+after+filename

for i in range(24):
    os.system(make_string(i+4324))
    time.sleep(10)