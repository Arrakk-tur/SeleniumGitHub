# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(60)
    request.addfinalizer(wd.quit)
    return wd


def test_LitecartLogin(driver):
    wd = driver
    wd.get("http://localhost/litecart/admin")
    wd.find_element_by_name('username').click()
    wd.find_element_by_name('username').clear()
    wd.find_element_by_name('username').send_keys('admin')
    wd.find_element_by_name('password').click()
    wd.find_element_by_name('password').clear()
    wd.find_element_by_name('password').send_keys('admin')
    # wd.find_element_by_css_selector('button.btn.btn-default').click()
    wd.find_element_by_name('login').click()
    wd.find_element_by_css_selector('[id="app-"] > a').click()
