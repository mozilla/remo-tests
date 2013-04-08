#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.base import Base


class About(Base):

    _page_title = 'Mozilla Reps - About'
    _about_sidebar_locator = (By.CSS_SELECTOR, '#about-navigation')
    _about_content_locator = (By.CSS_SELECTOR, '#about-text h3')

    def go_to_about_page(self):
        self.selenium.get(self.base_url + '/about/')
        self.is_the_current_page

    @property
    def is_about_sidebar_visible(self):
        return self.is_element_visible(*self._about_sidebar_locator)

    @property
    def is_about_content_visible(self):
        return self.find_element(*self._about_content_locator).text
