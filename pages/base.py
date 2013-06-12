#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from pages.page import Page, PageRegion


class Base(Page):

    _browserid_login_locator = (By.CSS_SELECTOR, '#browserid')
    _logout_menu_item_locator = (By.CSS_SELECTOR, '.hide-on-phones > a[href*="logout"]')
    _page_header_locator = (By.CSS_SELECTOR, 'header')

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
        WebDriverWait(self.selenium, self.timeout).until(lambda s: self.is_element_visible(*self._page_header_locator))

    class Header(Page):

        _events_locator = (By.CSS_SELECTOR, '#navigation-box li:nth-child(3) a')
        _faq_locator = (By.CSS_SELECTOR, '#navigation-box li:nth-child(7) a')
        _main_menu_locator = (By.CSS_SELECTOR, '#navigation-box > ul.nav-bar > li > a')

        @property
        def main_menu(self):
            return [self.MainMenu(self.testsetup, item) for item in self.find_elements(*self._main_menu_locator)]

        def click_events_link(self):
            self.selenium.find_element(*self._events_locator).click()
            from pages.events import Events
            return Events(self.testsetup)

        def click_faq_link(self):
            self.selenium.find_element(*self._faq_locator).click()
            from pages.faq import FAQ
            return FAQ(self.testsetup)

        class MainMenu(PageRegion):

            @property
            def text(self):
                return self._root_element.text

            def click(self):
                self._root_element.click()
