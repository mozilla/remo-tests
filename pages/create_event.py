#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from time import time,sleep

from pages.base import Base
from pages.event_detail import EventDetail


class CreateEvent(Base):

    _country_locator = (By.CSS_SELECTOR, 'id_country.current a')
    _event_category_locator = (By.CSS_SELECTOR, '[data-reveal-id="category-modal"]')
    _event_category_modal_save_locator = (By.CSS_SELECTOR, 'button.small:nth-child(5)')
    _event_choose_categories_locator = (By.ID, 'Addons-bit')
    _event_city_locator = (By.ID, 'id_city')
    _event_country_locator = (By.ID, 'id_country')
    _event_description_locator = (By.ID, 'id_description')
    _event_end_day_locator = (By.ID, 'id_end_form_0_day')
    _event_end_month_locator = (By.ID, 'id_end_form_0_month')
    _event_end_year_locator = (By.ID, 'id_end_form_0_year')
    _event_estimated_attendance_locator = (By.ID, 'id_estimated_attendance')
    _event_metric_locator = (By.ID, 'id_metrics-0-title')
    _event_metric2_locator = (By.ID, 'id_metrics-1-title')
    _event_name_locator = (By.ID, 'id_name')
    _event_owner_locator = (By.CSS_SELECTOR, 'id_owner_form.current a')
    _event_start_day_locator = (By.ID, 'id_start_form_0_day')
    _event_start_month_locator = (By.ID, 'id_start_form_0_month')
    _event_start_year_locator = (By.ID, 'id_start_form_0_year')
    _event_success_locator = (By.ID, 'id_metrics-0-outcome')
    _event_success2_locator = (By.ID, 'id_metrics-1-outcome')
    _event_timezone_locator = (By.CSS_SELECTOR, 'id_timezone.current a')
    _event_venue_locator = (By.ID, 'id_venue')
    _event_venue_map_button_locator = (By.CSS_SELECTOR, '[data-reveal-id="map-point"]')
    _event_venue_map_point_locator = (By.CSS_SELECTOR, 'img.leaflet-tile:nth-child(4)')
    _event_venue_map_save_button_locator = (By.CSS_SELECTOR, 'button.update:nth-child(1)')
    _save_event_button_locator = (By.CSS_SELECTOR, 'div.hide-for-small:nth-child(2) > button:nth-child(1)')


    def click_save_event_button(self, mozwebqa):
        self.selenium.find_element(*self._save_event_button_locator).click()
        return EventDetail(mozwebqa)

    def set_event_city(self, event_city):
        element = self.selenium.find_element(*self._event_city_locator)
        element.clear()
        element.send_keys(event_city)

    def set_event_country(self, option_country):
        element = self.selenium.find_element(*self._event_country_locator)
        select = Select(element)
        select.select_by_value(option_country)

    def set_event_description(self, event_description):
        element = self.selenium.find_element(*self._event_description_locator)
        element.clear()
        element.send_keys(event_description)

    def set_event_metric(self, event_metric):
        element = self.selenium.find_element(*self._event_metric_locator)
        element.clear()
        element.send_keys(event_metric)

    def set_event_metric2(self, event_metric2):
        element = self.selenium.find_element(*self._event_metric2_locator)
        element.clear()
        element.send_keys(event_metric2)

    def set_event_name(self, event_name):
        element = self.selenium.find_element(*self._event_name_locator)
        element.clear()
        element.send_keys(event_name)

    def set_event_success_metric(self, event_success):
        element = self.selenium.find_element(*self._event_success_locator)
        element.clear()
        element.send_keys(event_success)

    def set_event_success_metric2(self, event_success2):
        element = self.selenium.find_element(*self._event_success2_locator)
        element.clear()
        element.send_keys(event_success2)

    def set_event_venue(self, event_venue):
        element = self.selenium.find_element(*self._event_venue_locator)
        element.clear()
        element.send_keys(event_venue)

    def set_event_venue_map(self):
        self.selenium.find_element(*self._event_venue_map_button_locator).click()
        for handle in self.selenium.window_handles:
            self.selenium.switch_to_window(handle)
            WebDriverWait(self.selenium, self.timeout).until(lambda s: s.title)
        self.selenium.find_element(*self._event_venue_map_point_locator).click
        self.selenium.find_element(*self._event_venue_map_save_button_locator).click()

    def set_start_month(self, option_month):
        element = self.selenium.find_element(*self._event_start_month_locator)
        select = Select(element)
        select.select_by_value(option_month)

    def set_start_day(self, option_day):
        element = self.selenium.find_element(*self._event_start_day_locator)
        select = Select(element)
        select.select_by_value(option_day)

    def set_start_year(self, option_year):
        element = self.selenium.find_element(*self._event_start_year_locator)
        select = Select(element)
        select.select_by_value(option_year)

    def set_end_month(self, option_month):
        element = self.selenium.find_element(*self._event_end_month_locator)
        select = Select(element)
        select.select_by_value(option_month)

    def set_end_day(self, option_day):
        element = self.selenium.find_element(*self._event_end_day_locator)
        select = Select(element)
        select.select_by_value(option_day)

    def set_end_year(self, option_year):
        element = self.selenium.find_element(*self._event_end_year_locator)
        select = Select(element)
        select.select_by_value(option_year)

    def set_estimated_attendance(self, option_size):
        element = self.selenium.find_element(*self._event_estimated_attendance_locator)
        select = Select(element)
        select.select_by_value(option_size)

    def set_event_category(self):
        self.selenium.find_element(*self._event_category_locator).click()
        for handle in self.selenium.window_handles:
            self.selenium.switch_to_window(handle)
            WebDriverWait(self.selenium, self.timeout).until(lambda s: s.title)

        self.selenium.find_element(*self._event_choose_categories_locator).click()
        self.selenium.find_element(*self._event_category_modal_save_locator).click()
