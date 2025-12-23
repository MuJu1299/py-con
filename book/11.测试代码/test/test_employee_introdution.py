import pytest
from employee_introdution import Employee

def test_give_default_raise():
    '''测试错误的加薪'''
    bon_news=Employee('Bon','Jan',8000)
    bon_news.give_raise(2000)
    assert bon_news.salary==10000