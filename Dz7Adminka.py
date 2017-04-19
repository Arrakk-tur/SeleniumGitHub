# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver
import Dz2LitecartLogin


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(60)
    request.addfinalizer(wd.quit)
    return wd


def test_7Adminka(driver):
    login = Dz2LitecartLogin.test_LitecartLogin(driver)
    d = driver
    items = d.find_element_by_css_selector("#box-apps-menu").find_elements_by_tag_name("a")
    links = []
    for item in items:
        links.append(item.get_attribute("href"))
    for link in links:
        d.find_element_by_xpath('//a[@href="' + link + '"]').click()
        submenu = d.find_element_by_css_selector("#box-apps-menu").find_element_by_css_selector("li#app-.selected")
        subitems = submenu.find_elements_by_tag_name("a")
        sublinks = []
        for subitem in subitems:
            sublinks.append(subitem.get_attribute("href"))
        for sublink in sublinks:
            d.find_element_by_xpath('//a[@href="' + sublink + '"]').click()
            d.find_element_by_css_selector("h1")
