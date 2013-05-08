#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from pages.base import Base


class People(Base):

    _page_title = 'Mozilla Reps - People'
    _name_locator = (By.CSS_SELECTOR, '#grid-search-list.block-grid > li.profiles-li-item')
    _open_profile_locator = (By.CSS_SELECTOR, '#grid-search-list.block-grid > li.profiles-li-item > a')
    _people_filter_locator = (By.CSS_SELECTOR, '#searchfield.input-text')
    _people_map_locator = (By.CSS_SELECTOR, '#map')
    _people_name_text_locator = (By.CSS_SELECTOR, '.grid-profile-text > h6:first-child')
    _profile_grid_locator = (By.CSS_SELECTOR, '#profiles_gridview')
    _profile_image_locator = (By.CSS_SELECTOR, '#grid-search-list img')

    def go_to_people_page(self):
        self.selenium.get(self.base_url + '/people/')
        self.is_the_current_page
        WebDriverWait(self.selenium, self.timeout).until(lambda s: not s.find_element_by_id('canvasLoader').is_displayed())

    def filter_for(self, search_term):
        element = self.selenium.find_element(*self._people_filter_locator)
        element.send_keys(search_term)
        WebDriverWait(self.selenium, self.timeout).until(lambda s: not s.find_element_by_id('canvasLoader').is_displayed())

    def click_to_open_profile(self):
        self.selenium.find_element(*self._open_profile_locator).click()
        from pages.profile import Profile
        return Profile(self.testsetup)

    @property
    def people_name_text(self):
        return self.selenium.find_element(*self._people_name_text_locator).text

    @property
    def is_people_map_visible(self):
        return self.is_element_visible(*self._people_map_locator)

    @property
    def is_profile_grid_visible(self):
        return self.is_element_visible(*self._profile_grid_locator)

    @property
    def is_profile_name_visible(self):
        return self.is_element_visible(*self._name_locator)

    @property
    def is_profile_image_visible(self):
        return self.is_element_visible(*self._profile_image_locator)
