#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


from selenium.webdriver.common.by import By

from pages.page import Page
from pages.base import Base


class FAQ(Base):
    
    _faq_sidebar = (By.CSS_SELECTOR, '#about-navigation')

    def go_to_faqpage(self):
        self.selenium.get(self.testsetup.base_url + '/faq/')

    @property
    def is_faq_sidebar_visible(self):
        return self.is_element_visible(*self._faq_sidebar)
        