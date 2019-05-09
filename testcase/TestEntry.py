# coding=utf-8
'''
Created on 20190509

@author: linkswei
'''
import unittest

from testcase.TestFizz2AndBuzz4 import TestFizz2AndBuzz4
from testcase.TestFizz3AndBuzz5 import TestFizz3AndBuzz5


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(
        unittest.TestLoader().loadTestsFromTestCase(TestFizz2AndBuzz4))
    suite.addTests(
        unittest.TestLoader().loadTestsFromTestCase(TestFizz3AndBuzz5))

    runner = unittest.TextTestRunner()
    runner.run(suite)
