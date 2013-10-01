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
    _editable_monthly_reports_locator = (By.CSS_SELECTOR, '.mreports > li.editable a')
    _existing_monthly_reports_locator = (By.CSS_SELECTOR, '.mreports > li.exists a')

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

    @property
    def editable_monthly_reports_present(self):
        return self.is_element_present(*self._editable_monthly_reports_locator)

    def click_random_editable_monthly_reports(self):
        random.choice(self.find_elements(*self._editable_monthly_reports_locator)).click()
        return EditReport(self.testsetup)

    def click_random_existing_monthly_reports(self):
        random.choice(self.find_elements(*self._existing_monthly_reports_locator)).click()
        return EditReport(self.testsetup)


class EditReport(Base):

    _page_title = 'Mozilla Reps - Edit Report'

    _report_fields_locator = (By.CSS_SELECTOR, 'textarea.flat')
    _save_report_button_locator = (By.CSS_SELECTOR, '.reports-submit-button')
    _success_message_locator = (By.CSS_SELECTOR, '.alert-box.success')
    _activity_description_locator = (By.CSS_SELECTOR, '.tip-right[name="reportlink_set-0-description"]')
    _event_name_locator = (By.CSS_SELECTOR, 'input.tip-left[name="reportevent_set-0-name"]')
    _type_of_participation_locator = (By.ID, 'id_reportevent_set-0-participation_type')
    _event_link_locator = (By.CSS_SELECTOR, 'input.tip-left[name="reportevent_set-0-link"]')
    _activity_link_locator = (By.CSS_SELECTOR, 'input.tip-right[name="reportlink_set-0-link"]')
    _edit_report_button_locator = (By.CSS_SELECTOR, '.button[href*="edit"]')
    _delete_report_button_locator = (By.CSS_SELECTOR, '.button.alert[data-reveal-id="delete-report"]')
    _delete_report_warning_locator = (By.ID, 'delete-report')
    _popup_delete_button_locator = (By.CSS_SELECTOR, '.large.button.alert')

    def click_save_report_button(self):
        self.find_element(*self._save_report_button_locator).click()

    def click_edit_report_button(self):
        self.find_element(*self._edit_report_button_locator).click()

    def delete_report(self):
        self.find_element(*self._delete_report_button_locator).click()
        WebDriverWait(self.selenium, self.timeout).until(lambda s: self.is_element_visible(*self._delete_report_warning_locator))
        self.find_element(*self._popup_delete_button_locator).click()

    @property
    def is_success_message_visible(self):
        return self.is_element_visible(*self._success_message_locator)

    @property
    def success_message_text(self):
        return self.find_element(*self._success_message_locator).text

    def set_input_text_for(self, for_field, value):
        input_field = self.selenium.find_element(*getattr(self, '_%s_locator' % for_field))
        input_field.clear()
        input_field.send_keys(value)

    def select_type_of_participation(self, option_value):
        element = self.selenium.find_element(*self._type_of_participation_locator)
        select = Select(element)
        select.select_by_value(option_value)

    @property
    def report_fields(self):
        return [self.ReportSection(self.testsetup, web_element)
                for web_element in self.selenium.find_elements(*self._report_fields_locator)]

    class ReportSection(Page):

        def __init__(self, testsetup, element):
            Page.__init__(self, testsetup)
            self._root_element = element

        def type_value(self, value):
            self._root_element.send_keys(value)

        def clear_field(self):
            self._root_element.clear()


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
