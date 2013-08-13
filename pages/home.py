#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from pages.base import Base


class Home(Base):

    _page_title = "Mozilla Reps"

    _promo_box_locator = (By.CSS_SELECTOR, '.active > img')

    def __init__(self, testsetup, open_url=True):
        Base.__init__(self, testsetup)
        if open_url:
            self.selenium.get(self.base_url)
        WebDriverWait(self.selenium, self.timeout).until(lambda s: s.find_element(*self._promo_box_locator))

    def go_to_homepage(self):
        self.selenium.get(self.base_url)

    @property
    def get_favicon_url(self):
        r = requests.get(self.base_url, verify=False)
        html = BeautifulSoup(r.content)
        return html.find(attrs={'rel': 'shortcut icon'}).get('href')
