# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver

import Dz2LitecartLogin


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_7Adminka(driver):
    login = Dz2LitecartLogin.test_LitecartLogin(driver)
    d = driver
    menu = d.find_element_by_css_selector("#box-apps-menu")
    items = menu.find_elements_by_css_selector("#app-")
    print items
    i = items[0]
    for item in items:
        items[i] = item
        item.click
        # for item1 in items:
        #     item1 = d.find_element_by_css_selector("#app-")
        #     assert item1.get_attribute("class") == 'selected'
        i = i + 1
        print item
        # subitems = d.find_elements_by_css_selector("doc-template")
        # for subitem in subitems:
        #     i = subitems[0]
        #     subitems[i] = subitem.find_element_by_css_selector("a").click
        #     for subitem1 in subitems:
        #         subitem1 = d.find_element_by_css_selector("doc-template")
        #         assert subitem1.get_attribute("class") == 'selected'
        #         i = i + 1
        #     print subitem1
