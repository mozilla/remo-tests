#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.base import Base


class About(Base):

    _page_title = 'Mozilla Reps - About'
    _about_page_header_locator = (By.CSS_SELECTOR, '#about-text h1')
    _about_page_text_locator = (By.CSS_SELECTOR, '#about-text > p')
    _about_sidebar_faq_locator = (By.CSS_SELECTOR, '#about-navigation a[href*="faq"]')
    _about_sidebar_wiki_locator = (By.CSS_SELECTOR, '#about-navigation a[href*="wiki"]')

    def go_to_about_page(self):
        self.open('/about/')
        self.is_the_current_page

    @property
    def is_about_page_header_visible(self):
        return self.find_element(*self._about_page_header_locator).text

    @property
    def is_about_page_text_visible(self):
        return self.find_element(*self._about_page_text_locator)

    @property
    def is_about_sidebar_faq_visible(self):
        return self.is_element_visible(*self._about_sidebar_faq_locator)

    @property
    def is_about_sidebar_wiki_link_visible(self):
        return self.is_element_visible(*self._about_sidebar_wiki_locator)
