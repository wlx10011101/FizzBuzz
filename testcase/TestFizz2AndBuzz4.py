# coding=utf-8
'''
Created on 20190509

@author: linkswei
'''
import unittest

from src.Student import Student


class TestFizz2AndBuzz4(unittest.TestCase):

    def setUp(self):
        self.student = Student(2, 4)

    def test4ExpectFizzBuzz(self):
        gameResult = self.student.game(4)
        expectResult = "FizzBuzz"
        assert gameResult == expectResult, "expect: " + \
            expectResult + " , But get: " + gameResult\


    def test6ExpectFizz(self):
        gameResult = self.student.game(4)
        expectResult = "FizzBuzz"
        assert gameResult == expectResult, "expect: " + \
            expectResult + " , But get: " + gameResult


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
