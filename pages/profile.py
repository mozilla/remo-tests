#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.base import Base


class Profile(Base):

    _page_source = (By.CSS_SELECTOR, '#wrapper')
    _page_title = (By.CSS_SELECTOR, 'title:contains("Profile")')

    def go_to_people_page(self):
        self.selenium.get(self.base_url + '/people/')
        self.is_the_current_page

    @property
    def is_text_present(self):
        return self.selenium.find_element(*self._page_source).text
