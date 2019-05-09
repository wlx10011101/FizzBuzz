# coding=utf-8
'''
Created on 20190508

@author: linkswei
'''


class Student(object):
    '''
    classdocs
    '''

    def __init__(self, fizzNum, buzzNum):
        '''
        Constructor
        '''
        self.fizzNum = fizzNum
        self.buzzNum = buzzNum

    def game(self, indexOfSequence):
        result = ""
        if indexOfSequence % self.fizzNum == 0:
            result += "Fizz"
        if indexOfSequence % self.buzzNum == 0:
            result += "Buzz"
        if str(self.fizzNum) in str(indexOfSequence):
            result += "Fizz"
        if str(self.buzzNum) in str(indexOfSequence):
            result += "Buzz"
        if result == "":
            result = str(indexOfSequence)
        return result
