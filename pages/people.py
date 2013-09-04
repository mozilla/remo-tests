#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.base import Base


class People(Base):

    _page_title = 'Mozilla Reps - People'
    _page_loader_locator = (By.ID, 'canvasLoader')
    _name_locator = (By.CSS_SELECTOR, '.profiles-li-item')
    _open_profile_locator = (By.CSS_SELECTOR, '.profiles-li-item > a')
    _people_filter_locator = (By.ID, 'searchfield')
    _people_map_locator = (By.ID, 'map')
    _people_name_text_locator = (By.CSS_SELECTOR, '.grid-profile-text > h6')
    _profile_image_locator = (By.CSS_SELECTOR, '#grid-search-list img')
    _profile_grid_locator = (By.ID, 'profiles_gridview')
    _profile_list_locator = (By.ID, 'profiles_listview')
    _list_view_button_locator = (By.ID, 'listviewbutton')

    def filter_for(self, search_term):
        element = self.selenium.find_element(*self._people_filter_locator)
        element.send_keys(search_term)
        self.wait_for_page_to_load()

    def click_to_open_profile(self):
        self.selenium.find_element(*self._open_profile_locator).click()
        from pages.profile import Profile
        return Profile(self.testsetup)

    def click_list_view(self):
        self.selenium.find_element(*self._list_view_button_locator).click()

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

    @property
    def is_profile_list_visible(self):
        return self.is_element_visible(*self._profile_list_locator)
