#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from pages.base import Base


class NotFound(Base):

    _404_error_message_locator = (By.CSS_SELECTOR, '[id="404-error"] h2')

    def go_to_inexisting_page(self):
        self.open('/dummy')

    @property
    def is_404_error_message_visible(self):
        return self.is_element_visible(*self._404_error_message_locator)

    def get_error_message(self):
        return self.find_element(*self._404_error_message_locator).text
