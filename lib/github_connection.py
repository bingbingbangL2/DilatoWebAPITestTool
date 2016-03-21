'''
Created on Mar 18, 2016

@author: bxia
'''
from https_connection import HttpsConnection

class GitHubConnection(object):
    '''
    classdocs
    '''
    

    def __init__(self, ip, username = "bingbingbangL2", password = "2wsx#EDC", port = 443):
        '''
        Constructor
        '''
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password
        self.APIConnection = None
        self._APIConnect()
        
    def _APIConnect(self):
        self.APIConnection = HttpsConnection(self.ip, self.username, self.password, self.port)
        if self.APIConnection:
            return self.APIConnection
        else:
            self._APIConnect()
            return self.APIConnection