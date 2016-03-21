'''
Created on Mar 15, 2016

@author: bxia
'''

import threading
import Queue
import time
from logger import getLogger

_logger = getLogger()

class ThreadPool():
    def __init__(self, worknumber = 10, name = "Pool"):
        self.name = name
        self.size = worknumber
        self.jobqueue = Queue.Queue()
#         self.threadqueue = Queue.Queue()
        
    def addjob(self, func, *args, **kwargs):
        self.jobqueue.put((func, args, kwargs))
    def runjob(self):
        exitflag = False
        while True:
            func, args, kwargs = self.jobqueue.get()
            try:
                if func:
                    func(*args, **kwargs)
                else:
                    exitflag = True
            except Exception, ex:
                print ex
            finally:
                self.jobqueue.task_done()
                if exitflag:
                    break

    def work(self):
        for i in range(self.size):
            t = threading.Thread(target=self.runjob, name="Thread-%s" % str(i))
            t.setDaemon(True)
            t.start()
#             self.threadqueue.put(t)

    def waitcomplete(self):
        self.jobqueue.join()

    def reset(self):
        if self.jobqueue.empty():
            for i in range(self.size):
                self.addjob(None)
            self.jobqueue.join()
        else:
            raise Exception("Thread Pool % is still working, cannot reset" % self.name)


def printYourName(user = 'bingbingbang_Level_2'):
    user += '\n'
    _logger.info(user)
    time.sleep(5)
    
if __name__ == '__main__':
    tp = ThreadPool()
    for i in range(20):
        tp.addjob(func = printYourName, user = "bingbingbang_level_up")
#         tp.addjob(printYourName, "bingbingbang_level_up")
    tp.work()
    tp.waitcomplete()
        
    
    
    
    