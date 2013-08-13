#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from pages.base import Base
from pages.event_detail import EventDetail


class EditEvent(Base):

    _description_field_locator = (By.ID, 'id_description')
    _save_event_button = (By.CSS_SELECTOR, '.four.columns.align-right.hide-on-phones button')

    def edit_event_description(self, new_description):
        element = self.selenium.find_element(*self._description_field_locator)
        element.clear()
        element.send_keys(new_description)

    def click_save_event_button(self):
        self.selenium.find_element(*self._save_event_button).click()
        return EventDetail(self.testsetup)
