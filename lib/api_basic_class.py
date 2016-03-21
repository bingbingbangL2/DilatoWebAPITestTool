#-*-coding:UTF-8-*-
'''
Created on Mar 17, 2016

@author: bxia
'''

import json
import urllib,urllib2
from urllib import urlencode
import base64
from logger import getLogger
from github_connection import GitHubConnection


METHOD_GET = 'GET'
METHOD_POST = 'POST'
METHOD_PUT = 'PUT'
METHOD_DELETE = 'DELETE'
METHOD_PATCH = 'PATCH'

TESTCASE_RESULT_FORMAT = "Response Code: %d, Response content: %s"

_logger = getLogger()


class APIResquest():
    DEFAULT_VERSION = 'v1'
    def __init__(self, github, url, method):
#         self.connection = None
        self.github = github
        self.connection = github.APIConnection
        self.url = url
        self.method = method
        self.headers = {}
        self.payload = None
        self.object_id = None
        self.url_parameters = None
        
        self.url_prefix = "/api/"
#          + self.DEFAULT_VERSION
    @staticmethod
    def get(github, url):
        return APIResquest(github, url, METHOD_GET)
    @staticmethod
    def post(github, url):
        return APIResquest(github, url, METHOD_POST)
    @staticmethod
    def put(github, url):
        return APIResquest(github, url, METHOD_PUT)
    @staticmethod
    def delete(github, url):
        return APIResquest(github, url, METHOD_DELETE)
    @staticmethod
    def patch(github, url):
        return APIResquest(github, url, METHOD_PATCH)
    
    def addheaders(self, header):
        self.headers = header
        return self
    
    def setdata(self, payload = "", object_id = None, url_parameters = {}):
#         if convert_JOSN:s
#             data = json.dumps(data)
        if payload and self.method in [METHOD_POST, METHOD_PUT]:
            if type(payload) is not str:
                payload = json.dumps(payload)
            self.payload = payload
        elif self.method == METHOD_GET:
            if object_id:
                self.object_id = object_id
                self.url = "%s/%s" %(self.url, object_id)
            else:
                pass
            self.url_parameters = url_parameters
        elif self.method == METHOD_DELETE:
            self.object_id = object_id
            
        return self
    
    def request(self):
        response = self._request(self.method, self.url, self.payload, self.url_parameters)
        
        return response
    
    def _request(self, method, endpoint, payload="",
                 url_parameters = None, request_timeout = None):
        #TODO; if need auth, implements later
#         auth = base64.urlsafe_b64encode(
#         self.github.username + ":" + self.github.password).decode(
#                 "ascii")
#         auth = {self.github.username: self.github.password}
#         if data and method is METHOD_GET:
#         headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
# #               'Accept': "application/json"
#         }
#         headers = {'Authorization': '%s' %(self.github.username) ,
# #                    'content-type': "application/json"
#         }
        

        url_parameters = {self.github.username :self.github.password}
        data = urllib.urlencode(url_parameters)

        request = urllib2.Request(endpoint)
        for key in self.headers.keys():
            request.add_header(key, self.headers.get(key))
#         request.get_method = lambda:self.method
        try:
            response = urllib2.urlopen(request, data)
        except Exception, ex:
            print ex
#         self.connection.create_connection(timeout=request_timeout)
#         url_params = ""
#         if url_parameters:
#             if "?" in endpoint:
#                 url_params = "&%s" % urlencode(url_parameters)
#             else:
#                 url_params = "?%s" % urlencode(url_parameters)
# 
#         request = "%s%s" % (endpoint, url_params)
#         print("DEBUG_request: %s %s" %(method, request))
#         if payload:
#             print("DEBUG_workload: %s" %payload)
#         
#         response = self.connection.request(method,
#                                                 request,
#                                                 payload,
#                                                 headers)
    
        return APIResponse(response)
 
class APIResponse():
    def __init__(self, response):
        self.response = response
    def assertCode(self):
        code = self.response.code
        result_string = self.response.read()
        py_dict = json.loads(result_string) if result_string else {}
        
        if code < 200 or code >= 300 :
            pass
#         or "error_code" in py_dict:
#             raise Exception(py_dict)
        else:
            return code, result_string

    def assertObject(self):
        content = self.response.read()
        
    
if __name__ == '__main__':
#     url = "https://api.douban.com/v2/book/user/ahbei/collections"
    url = "https://api.github.com/"
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
              'Accept': "application/json"}
#     data={'status':'read','rating':3,'tag':'小说'}
#     data={'status':'read','rating':3,'tag':'小说'}
#     response = APIResquest.get(url).addheaders(header).setdata(data).request()
#     result = response.assertCode()
#     _logger.info(result)
    '''
    Client ID
    9c5c6c816785c15f616a
    Client Secret
    
    '''
#     data = { "scope": ["bingbingbangL2","public_repo"], "state":"read",
#             "redirect_uri": "https://github.com/bingbingbangL2/resrful_api_test",
#             "client_id": "9c5c6c816785c15f616a"}
    
    github = GitHubConnection(url, username = "bingbingbangL2", password = "2wsx#EDC")
    
    testcase = APIResquest.get(github, "https://api.github.com/user").request().assertCode()
    result = TESTCASE_RESULT_FORMAT % (testcase[0], testcase[1])
    _logger.info(result)
    
#     url_2 = "https://github.com/login/oauth/access_token"
#     
#     data_2 = {"client_id": "9c5c6c816785c15f616a"}