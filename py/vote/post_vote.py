import time
import random
import requests

url = 'http://email.citydating23.top/vote.php'

code = random.randint(1001,9999)
print code
wechatid = random.randint(100000,999999)
print wechatid

time = int(time.time())
print time

j_time = int( (time+1)*1000 )
print j_time

d = {'aid': 292,
     'width': 800,
     'height':600,
     'id':12297,
     'wechatid':370774,
     #'wechatid':wechatid,
     'orther_id':'',
     'xenon':'oJkaj1Ee1aWJVF4QKD1rvC6sBpuE', #28 bit
     'code':code,
     'p_time':time,
     'j_time':j_time
        }
r = requests.post(url, data=d)
print r.text
