#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.base import Base


class Dashboard(Base):

    _success_message_locator = (By.CSS_SELECTOR, '.alert-box.success')
    _add_report_locator = (By.CSS_SELECTOR, '.small.button[href="/reports/new/"]')

    @property
    def is_success_message_visible(self):
        return self.is_element_visible(*self._success_message_locator)

    def click_add_new_report(self):
        self.selenium.find_element(*self._add_report_locator).click()
        self.selenium.switch_to_window(self.selenium.window_handles[1])
        from pages.profile import AddReport
        return AddReport(self.testsetup)
