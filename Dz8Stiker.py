# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(60)
    request.addfinalizer(wd.quit)
    return wd


def test_8Stiker(driver):
    d = driver
    d.get('http://localhost/litecart')
    elements = d.find_elements_by_css_selector(".product.column.shadow.hover-light")
    for elem in elements:
        len(elem.find_elements_by_css_selector('.sticker')) == 1
