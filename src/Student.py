# coding=utf-8
'''
Created on 20190508

@author: linkswei
'''
from src.FizzBuzzGame import FizzBuzzGame


class Student(object):
    '''
    classdocs
    '''

    def __init__(self, fizzNum, buzzNum):
        '''
        Constructor
        '''
        self.gameRuler = FizzBuzzGame(fizzNum, buzzNum)

    def game(self, num):
        result = ""
        if num < 1:
            return result
        if self.gameRuler.isFizzBuzz(num):
            result += "FizzBuzz"
            return result
        if self.gameRuler.isFizz(num):
            result += "Fizz"
        if self.gameRuler.isBuzz(num):
            result += "Buzz"
        if result == "":
            return str(num)
        else:
            return result
