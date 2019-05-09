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

    def test0Expectnull(self):
        gameResult = self.student.game(0)
        expectResult = ""
        assert gameResult == expectResult, "expect: " + \
            expectResult + " , But get: " + gameResult

    def test1Expect1(self):
        gameResult = self.student.game(1)
        expectResult = "1"
        assert gameResult == expectResult, "expect: " + \
            expectResult + " , But get: " + gameResult

    def test3ExpectFizz(self):
        gameResult = self.student.game(3)
        expectResult = "Fizz"
        assert gameResult == expectResult, "expect: " + \
            expectResult + " , But get: " + gameResult

    def test13ExpectFizz(self):
        gameResult = self.student.game(13)
        expectResult = "Fizz"
        assert gameResult == expectResult, "expect: " + \
            expectResult + " , But get: " + gameResult

    def test15ExpectFizzBuzz(self):
        gameResult = self.student.game(15)
        expectResult = "FizzBuzz"
        assert gameResult == expectResult, "expect: " + \
            expectResult + " , But get: " + gameResult

    def test5ExpectBuzz(self):
        gameResult = self.student.game(5)
        expectResult = "Buzz"
        assert gameResult == expectResult, "expect: " + \
            expectResult + " , But get: " + gameResult

    def test52ExpectBuzz(self):
        gameResult = self.student.game(52)
        expectResult = "Buzz"
        assert gameResult == expectResult, "expect: " + \
            expectResult + " , But get: " + gameResult

    def testRange1To100ExpectInList(self):
        for i in range(100):
            i += 1
            gameResult = self.student.game(i)
            assert gameResult in [str(i), "Fizz", "Buzz", "FizzBuzz"],\
                "gameResult Not in expect List, But get: " + gameResult


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
