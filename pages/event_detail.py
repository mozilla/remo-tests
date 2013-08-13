#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.base import Base


class EventDetail(Base):

    _edit_event_button = (By.CSS_SELECTOR, '.four.columns.align-right.hide-on-phones > a:nth-child(3)')
    _event_description_locator = (By.CSS_SELECTOR, '.profile-item:nth-child(2)')
    _event_saved_message_locator = (By.CSS_SELECTOR, '.alert-box.success')

    def click_edit_event_button(self):
        self.selenium.find_element(*self._edit_event_button).click()
        from pages.edit_event import EditEvent
        return EditEvent(self.testsetup)

    @property
    def description(self):
        return self.selenium.find_element(*self._event_description_locator).text

    @property
    def event_saved_message(self):
        return self.selenium.find_element(*self._event_saved_message_locator)
