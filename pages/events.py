#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.base import Base


class Events(Base):

    _page_title = 'Mozilla Reps - Events'
    _events_map_locator = (By.CSS_SELECTOR, '#map')
    _events_table_locator = (By.CSS_SELECTOR, '#events-table-body')
    _events_filter_locator = (By.CSS_SELECTOR, '#searchfield')
    _events_result_locator = (By.CSS_SELECTOR, '.event-item')

    def go_to_events_page(self):
        self.selenium.get(self.base_url + '/events/')
        self.is_the_current_page

    @property
    def is_events_map_visible(self):
        return self.is_element_visible(*self._events_map_locator)

    @property
    def is_events_table_visible(self):
        return self.is_element_visible(*self._events_table_locator)

    @property
    def is_filter_result_visible(self):
        return self.is_element_visible(*self._events_result_locator)

    def filter_for(self, search_term):
        element = self.selenium.find_element(*self._events_filter_locator)
        element.send_keys(search_term)
