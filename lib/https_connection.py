'''
Created on Mar 18, 2016

@author: bxia
'''
from connection import Connection
import httplib



class HttpsConnection(Connection):
    '''
        extends Connection, Use HTTP connect server
    '''
    def __init__(self, ip, username = None, password = None, port = 443):
        '''
            
        '''
        super(HttpsConnection, self).__init__(ip, username, password)
        self.port = port
        self.protocal = 'https'
        
    def create_connection(self, timeout = None):
        timeout = Connection.DEFAULT_REQUEST_TIMEOUT if timeout is None else timeout
#         if sys.version_info >= (2,7,9):
#             ctx = ssl._create_unverified_context()
#             self.anchor = httplib.HTTPSConnection(self.ip, self.port,
#                                                   context=ctx,
#                                                   timeout=timeout)
        self.anchor = httplib.HTTPConnection(self.ip, self.port,
                                                  timeout=timeout)
        