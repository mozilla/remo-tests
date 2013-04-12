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

    _account_locator = (By.CSS_SELECTOR, '#login-box.ten > ul > li.account > div.hide-on-phones')
    _signin_locator = (By.CSS_SELECTOR, '#browserid')

    def go_to_homepage(self):
        self.selenium.get(self.base_url)

    @property
    def is_account_loggedin(self):
        return self.is_element_visible(*self._account_locator)

    @property
    def is_account_loggedout(self):
        return self.is_element_visible(*self._signin_locator)

    def get_favicon_url(self):
        r = requests.get(self.base_url, verify=False)
        html = BeautifulSoup(r.content)
        return html.find(attrs={'rel': 'shortcut icon'}).get('href')
