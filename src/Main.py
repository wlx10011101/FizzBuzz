# coding=utf-8
'''
Created on 20190508

@author: linkswei
'''
from src.Student import Student


def FizzAndBuzz(FizzNum, BuzzNum):
    student = Student(FizzNum, BuzzNum)
    for i in range(100):
        print student.game(i)


if __name__ == "__main__":
    FizzAndBuzz(3, 5)
