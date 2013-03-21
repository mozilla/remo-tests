#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.base import Base


class Events(Base):

    _page_title = 'Mozilla Reps - Events'
    _events_map_locator = (By.CSS_SELECTOR, '#map')

    def go_to_events_page(self):
        self.selenium.get(self.base_url + '/events/')
        self.is_the_current_page

    @property
    def is_events_map_visible(self):
        return self.is_element_visible(*self._events_map_locator)
