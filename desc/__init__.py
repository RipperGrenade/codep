__all__ = ['descriptortest']

import threading
import random
import time


class DescClass(threading.Thread):
    __name = 'selfclass'

    def __init__(self, count, lockname):
        threading.Thread.__init__(self)
        self.count = count
        self.lockname = lockname

    def run(self):
        print('threading running with {0} and {1}'.format(self.count, self.lockname))
        print(self.__dict__)
        time.sleep(random.randint(1, 10))
