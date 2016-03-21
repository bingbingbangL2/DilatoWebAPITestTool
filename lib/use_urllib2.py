#-coding:UTF8-*-
'''
Created on Mar 16, 2016

@author: bxia
'''


import urllib, urllib2
import json 
import time
from ThreadPool import ThreadPool
from logger import getLogger


SERVER_ADDR = "https://%s:%s"
_logger = getLogger()


def dataEncodeJSON(arg):
    data = json.dumps(arg, ensure_ascii=False)
    return data

def dataDecodeJSON(json_arg):
    data = json.loads(json_arg)
    return data

def connect(ip, port = 443, user = None, passwd = None):
    server_ip = SERVER_ADDR % (ip, str(port))
    '''
    
    '''

# def 

def apitest(url, data):
    
#     url = 'http://localhost:8888/'
#     data={'who': '夏冰'}
    data = urllib.urlencode(data)
    
    request = urllib2.Request(url, data)
#     request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36')
    

#     headers = {'Content-Type': 'application/json; charset=UTF-8'}
    
    response = urllib2.urlopen(request)
    apicontent = response.read()
    
#     if i%8 == 1:
#         time.sleep(100)
#     else:
#         time.sleep(10)

    _logger.info("Response Code:%s, Response content:%s" %(str(response.code), apicontent))

if __name__ == '__main__':

#     arg = [[1,2,3], {1:"a", 2:'b'}, 1, 2, "wsx", (1,2,3), 1.2]   
#     data = dataEncodeJSON(arg)
#     decode_data = dataDecodeJSON(data)
    tp = ThreadPool()
#     print len('夏冰')
    for i in range(1):
#         tp.addjob(func = apitest, url = 'http://localhost:8888', data = {'who': '夏冰'})
#         string1 = '夏冰'
#         content = {}
#         content.setdefault('name')
#         content['name'] = '{}'.format(string1)
#         data = {'who': content}
#         content = {'name': '夏冰', 'respobility': 'tester'}
        url = "https://api.douban.com/v2/book/user/ahbei/collections"
        header = None
        data={'status':'read','rating':3,'tag':'小说'}
        tp.addjob(func = apitest, url = url, data = data)
    tp.work()
    tp.waitcomplete()
    pass