# coding=utf-8
'''
Created on 20190509

@author: linkswei
'''


class FizzBuzzGame(object):
    '''
    classdocs
    '''

    def __init__(self, fizzNum, buzzNum):
        '''
        Constructor
        '''
        self.fizzNum = fizzNum
        self.buzzNum = buzzNum

    def isFizz(self, num):
        if num % self.fizzNum == 0 or str(self.fizzNum) in str(num):
            return True
        else:
            return False

    def isBuzz(self, num):
        if num % self.buzzNum == 0 or str(self.buzzNum) in str(num):
            return True
        else:
            return False

    def isFizzBuzz(self, num):
        if num % self.fizzNum == 0 and num % self.buzzNum == 0:
            return True
        else:
            return False
