#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

from pages.base import Base
from pages.page import Page


class Profile(Base):

    _page_source_locator = (By.ID, 'wrapper')
    _user_avatar_locator = (By.ID, 'profiles-view-avatar')
    _edit_profile_button_locator = (By.CSS_SELECTOR, '.small.button')
    _update_message_locator = (By.CSS_SELECTOR, '.alert-box.success')

    def __init__(self, testsetup):
        Base.__init__(self, testsetup)
        self.wait_for_element_visible(*self._user_avatar_locator)

    @property
    def profile_text(self):
        return self.selenium.find_element(*self._page_source_locator).text

    def click_edit_profile(self):
        self.selenium.find_element(*self._edit_profile_button_locator).click()
        return EditProfile(self.testsetup)

    @property
    def is_update_message_visible(self):
        return self.is_element_visible(*self._update_message_locator)

class AddReport(Base):
    
    _page_title = 'Mozilla Reps - Add Report'

    _save_report_button_locator = (By.CSS_SELECTOR, '.small.button.confirm')
    _activity_description_locator = (By.ID, 'id_activity_description')
    _event_name_locator = (By.CSS_SELECTOR, 'input.tip-left[name="reportevent_set-0-name"]')
    _activity_type_locator = (By.CSS_SELECTOR, '#id_activity')
    _campaign_locator = (By.ID, 'id_campaign')
    _event_link_locator = (By.CSS_SELECTOR, 'input.tip-left[name="reportevent_set-0-link"]')
    _activity_url_locator = (By.ID, 'id_link')
    _url_description_locator = (By.ID, 'id_link_description')
    _contribution_area_locator = (By.ID, 'id_functional_areas')
    _delete_report_button_locator = (By.CSS_SELECTOR, '.small.button.alert')
    _delete_report_warning_locator = (By.ID, 'delete-report')
    _popup_delete_button_locator = (By.CSS_SELECTOR, '.large.button.alert')
    _event_venue_locator = (By.ID, 'id_venue')
    _event_venue_map_button_locator = (By.CSS_SELECTOR, '[data-reveal-id="map-point"]')
    _event_venue_map_point_locator = (By.CSS_SELECTOR, 'img.leaflet-tile:nth-child(4)')
    _event_venue_map_save_button_locator = (By.CSS_SELECTOR, 'button.update:nth-child(1)')

    def select_activity(self, option_value):
        element = self.selenium.find_element(*self._activity_type_locator)
        select = Select(element)
        select.select_by_value(option_value)

    def select_campaign(self, option_value):
        element = self.selenium.find_element(*self._campaign_locator)
        select = Select(element)
        select.select_by_value(option_value)

    def select_contribution_area(self, option_text):
        element = self.selenium.find_element(*self._contribution_area_locator)
        select = Select(element)
        select.select_by_visible_text(option_text)

    def select_event_place(self):
        self.selenium.find_element(*self._event_venue_map_button_locator).click()
        for handle in self.selenium.window_handles:
            self.selenium.switch_to_window(handle)
            WebDriverWait(self.selenium, self.timeout).until(lambda s: s.title)
        self.selenium.find_element(*self._event_venue_map_point_locator).click
        self.selenium.find_element(*self._event_venue_map_save_button_locator).click()

    def type_url_for_activity(self, url):
        self.selenium.find_element(*self._activity_url_locator).send_keys(url)

    def type_url_description(self, description):
        self.selenium.find_element(*self._url_description_locator).send_keys(description)

    def type_activity_description(self, description):
        self.selenium.find_element(*self._activity_description_locator).send_keys(description)

    def click_save_report_button(self):
        self.find_element(*self._save_report_button_locator).click()
        return ViewReport(self.testsetup)

class ViewReport(Base):

    _edit_report_locator = (By.XPATH, './/*[@id="wrapper"]/div/main/div[1]/div[2]/a')
    _success_message_locator = (By.CSS_SELECTOR, '.alert-box.success')

    def click_edit_report(self):
        self.selenium.find_element(*self._edit_report_locator).click()
        return EditReport(self.testsetup)

    @property
    def is_success_message_visible(self):
        return self.is_element_visible(*self._success_message_locator)

    @property
    def success_message_text(self):
        return self.find_element(*self._success_message_locator).text

class EditReport(AddReport):

    _page_title = 'Mozilla Reps - Edit Report'

    _delete_report_button_locator = (By.CSS_SELECTOR, '.small.button.alert')
    _delete_report_warning_locator = (By.ID, 'ng-delete-report')
    _popup_delete_button_locator = (By.CSS_SELECTOR, '.large.button.alert')

    def delete_report(self):
        self.find_element(*self._delete_report_button_locator).click()
        WebDriverWait(self.selenium, self.timeout).until(lambda s: self.is_element_visible(*self._delete_report_warning_locator))
        self.find_element(*self._popup_delete_button_locator).click()
        return ViewReport(self.testsetup)

class EditProfile(Base):

    _page_title = 'Mozilla Reps - Edit Profile'

    _profile_fields_locator = (By.CSS_SELECTOR, '#name-gender > input')
    _save_profile_button_locator = (By.ID, 'save-profile-button')

    @property
    def profile_fields(self):
        return [self.ProfileSection(self.testsetup, web_element)
                for web_element in self.selenium.find_elements(*self._profile_fields_locator)]

    def click_save_profile(self):
        self.selenium.find_element(*self._save_profile_button_locator).click()
        return Profile(self.testsetup)

    class ProfileSection(Page):

        def __init__(self, testsetup, element):
            Page.__init__(self, testsetup)
            self._root_element = element

        @property
        def field_value(self):
            try:
                return self._root_element.get_attribute('value')
            except Exception.NoSuchAttributeException:
                return " "

        def type_value(self, value):
            if value != '':
                self._root_element.send_keys(value)

        def clear_field(self):
            self._root_element.clear()
