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
        assert(self.student.game(1) == "1")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
