#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.base import Base

class Settings(Base):
    
    _report_email_checkbox_locator = (By.CSS_SELECTOR, '#id_receive_email_on_add_comment ~ span')
    _events_email_checkbox_locator = (By.CSS_SELECTOR, '#id_receive_email_on_add_event_comment ~ span')
    _save_locator = (By.CSS_SELECTOR, '.hide-on-phones > #save-settings')

    def click_report_checkbox(self):
        self.selenium.find_element(*self._report_email_checkbox_locator).click()

    def click_events_checkbox(self):
        self.selenium.find_element(*self._events_email_checkbox_locator).click()

    def click_save(self):
        self.selenium.find_element(*self._save_locator).click()

    @property   
    def is_report_checked(self):
        return 'checked' in self.find_element(*self._report_email_checkbox_locator).get_attribute('class')

    @property
    def is_events_checked(self):
        return 'checked' in self.find_element(*self._events_email_checkbox_locator).get_attribute('class')