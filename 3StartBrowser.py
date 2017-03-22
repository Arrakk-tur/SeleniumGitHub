# -*- coding: utf-8 -*-
import pytest, time
from selenium import webdriver


# Uncomment what you need


# # Chrome
# @pytest.fixture
# def driver(request):
#     wd = webdriver.Chrome()
#     request.addfinalizer(wd.quit)
#     return wd
#
# # IE
# @pytest.fixture
# def driver(request):
#     wd = webdriver.Ie(capabilities={"requireWindowFocus": True})
#     request.addfinalizer(wd.quit)
#     return wd
#
# # Firefox
# @pytest.fixture
# def driver(request):
#     wd = webdriver.Firefox()
#     request.addfinalizer(wd.quit)
#     return wd

def test_1FirstTest1(driver):
    wd = driver
    wd.get("http://i.ua")
    time.sleep(3)
