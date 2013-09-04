#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


from selenium.webdriver.common.by import By

from pages.base import Base


class FAQ(Base):

    _faq_sidebar = (By.CSS_SELECTOR, '#about-navigation')

    def __init__(self, testsetup):
        Base.__init__(self, testsetup)
        self.wait_for_element_visible(*self._faq_sidebar)

    @property
    def is_faq_sidebar_visible(self):
        return self.is_element_visible(*self._faq_sidebar)
