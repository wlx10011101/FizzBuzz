# coding=utf-8
'''
Created on 20190509

@author: linkswei
'''
import unittest
from src.Student import Student


class TestFizz3AndBuzz5(unittest.TestCase):

    def setUp(self):
        self.student = Student(3, 5)

    def testIndexOfSequence1Expect1(self):
        gameResult = self.student.game(1)
        expectResult = "1"
        assert gameResult == expectResult, "expect: " + \
            expectResult + " , But get: " + gameResult

    def testIndexOfSequence3ExpectFizz(self):
        gameResult = self.student.game(3)
        expectResult = "Fizz"
        assert gameResult == expectResult, "expect: " + \
            expectResult + " , But get: " + gameResult


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
