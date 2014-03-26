#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from pages.page import Page


class Base(Page):

    _browserid_login_locator = (By.CSS_SELECTOR, '.browserid-login > span')
    _logout_menu_item_locator = (By.CSS_SELECTOR, '.hide-for-small .browserid-logout')
    _page_loader_locator = (By.ID, 'canvasLoader')

    @property
    def header(self):
        return self.Header(self.testsetup)

    @property
    def is_user_loggedin(self):
        return self.is_element_present(*self._logout_menu_item_locator)

    def click_browserid_login(self):
        self.selenium.find_element(*self._browserid_login_locator).click()

    def login(self, user='default'):
        self.click_browserid_login()
        credentials = self.testsetup.credentials[user]

        from browserid import BrowserID
        pop_up = BrowserID(self.selenium, self.timeout)
        pop_up.sign_in(credentials['email'], credentials['password'])
        WebDriverWait(self.selenium, self.timeout).until(lambda s: self.is_user_loggedin)

    def click_logout_menu_item(self):
        self.selenium.find_element(*self._logout_menu_item_locator).click()

    def wait_for_page_to_load(self):
        WebDriverWait(self.selenium, self.timeout).until(lambda s: self.is_element_not_visible(*self._page_loader_locator)
                                                         and self.selenium.execute_script('return jQuery.active == 0'))

    class Header(Page):

        _account_locator = (By.ID, 'base-displayname')
        _events_menu_locator = (By.CSS_SELECTOR, '#navigation-box li > a[href$="/events/"]')
        _faq_menu_locator = (By.CSS_SELECTOR, '#navigation-box li > a[href$="/faq/"]')
        _main_menu_locator = (By.CSS_SELECTOR, '#navigation-box > ul.nav-bar > li > a')
        _settings_locator = (By.CSS_SELECTOR, '.hide-for-small > a[href$="/settings/"]')
        _people_menu_locator = (By.CSS_SELECTOR, '#navigation-box li > a[href$="/people/"]')
        _planet_menu_locator = (By.CSS_SELECTOR, '#navigation-box li > a[href*="planet"]')
        _wiki_menu_locator = (By.CSS_SELECTOR, '#navigation-box li > a[href*="wiki"]')
        _dashboard_menu_locator = (By.CSS_SELECTOR, '#navigation-box li > a[href$="/dashboard/"]')

        @property
        def main_menu(self):
            return [self.MainMenu(self.testsetup, item) for item in self.find_elements(*self._main_menu_locator)]

        def click_events_link(self):
            self.selenium.find_element(*self._events_menu_locator).click()
            from pages.events import Events
            return Events(self.testsetup)

        def click_faq_link(self):
            self.selenium.find_element(*self._faq_menu_locator).click()
            from pages.faq import FAQ
            return FAQ(self.testsetup)

        def click_settings(self):
            self.selenium.find_element(*self._settings_locator).click()
            from pages.settings import Settings
            return Settings(self.testsetup)

        def click_people_link(self):
            self.selenium.find_element(*self._people_menu_locator).click()
            from pages.people import People
            return People(self.testsetup)

        def click_profile(self):
            self.selenium.find_element(*self._account_locator).click()
            from pages.profile import Profile
            return Profile(self.testsetup)

        def click_dashboard(self):
            self.selenium.find_element(*self._dashboard_menu_locator).click()
            from pages.dashboard import Dashboard
            return Dashboard(self.testsetup)
