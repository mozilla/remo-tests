#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from selenium.webdriver.common.by import By
from pages.base import Base


class NotFound(Base):

    _404_div = (By.XPATH, '//*[@id="404-error"]/h2')

    def go_to_inexisting_page(self):
        self.selenium.get(self.testsetup.base_url + '/dummy')

    @property
    def is_404_div_visible(self):
        return self.is_element_visible(*self._404_div)

    def get_404_text(self):
        return self.find_element(*self._404_div).text