'''
Created on Mar 18, 2016

@author: bxia
'''

class Connection(object):
    
    DEFAULT_REQUEST_TIMEOUT = 300
    
    '''
        Basic class for connection
    '''
    def __init__(self, ip, username = None, password = None):
        '''
            auchor
        '''
        self.ip = ip
        self.username = username
        self.password = password
        self.anchor = None 
        self.protocal = None
        
    def create_connection(self):
        raise NotImplemented
    
    def request(self, method, url, payload, headers):
        self.anchor.request(method, url, payload, headers)
        response = self.anchor.getresponse()
        return response