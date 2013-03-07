#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


from selenium.webdriver.common.by import By

from pages.page import Page
from pages.base import Base


class LabsPage(Base):

    _privacy_section_locator = (By.ID, 'privacy')

    def go_to_labspage(self):
        self.selenium.get(self.testsetup.base_url + '/labs/')
        self.is_the_current_page

    @property
    def is_privacy_section_present(self):
        return self.is_element_present(*self._privacy_section_locator)


