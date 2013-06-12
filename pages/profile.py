#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.base import Base


class Profile(Base):

    _page_source_locator = (By.ID, 'wrapper')
    _page_title_locator = (By.CSS_SELECTOR, 'title:contains("Profile")')
    _user_avatar_locator = (By.ID, 'profiles-view-avatar')

    def __init__(self, testsetup):
        Base.__init__(self, testsetup)
        self.wait_for_element_visible(*self._user_avatar_locator)

    @property
    def profile_text(self):
        return self.selenium.find_element(*self._page_source_locator).text
