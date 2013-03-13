#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


from selenium.webdriver.common.by import By

from pages.page import Page
from pages.base import Base


class Events(Base):

    _events_map_locator = (By.CSS_SELECTOR, '#map')

    def go_to_eventspage(self):
        self.selenium.get(self.testsetup.base_url + '/events/')

    @property
    def is_events_map_visible(self):
        return self.is_element_visible(*self._events_map_locator)
