# -*- coding: utf-8 -*-
import pytest, time
from selenium import webdriver



# Firefox
@pytest.fixture
def driver(request):
    wd = webdriver.Firefox(capabilities={"marionette": False})
    request.addfinalizer(wd.quit)
    return wd

def test_1FirstTest1(driver):
    wd = driver
    wd.get("http://i.ua")
    time.sleep(3)
