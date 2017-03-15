# -*- coding: utf-8 -*-

import unittest, time
from selenium import webdriver


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class FirstTest(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(60)

    def test_1FirstTest(self):
        success = True
        wd = self.wd
        wd.get("http://i.ua")
        time.sleep(3)
        self.assertTrue(success)

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
