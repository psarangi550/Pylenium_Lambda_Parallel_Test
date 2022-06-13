from pylenium.driver import Pylenium
import urllib3
import pytest

class TestPyleniumLambda(object):
    #defining the driver element
    
    def __init__(self,Pylenium):
        self.py=Pylenium

    def goto(self):
        self.py.visit("https://lambdatest.github.io/sample-todo-app/")
        return self
    
    def get_element(self):
        return self.py.getx("//input[@name='li1']")
    
    def get_all_elements(self):
        return self.py.findx("//input[@type='checkbox']")

@pytest.fixture
def page(py:Pylenium)->TestPyleniumLambda:
    return TestPyleniumLambda(py).goto()


def test_clickitem(page:TestPyleniumLambda):
    page.get_element().click()


def test_allitem(page:TestPyleniumLambda):
    all_elem=page.get_all_elements()
    for ele in all_elem:
        ele.click()
