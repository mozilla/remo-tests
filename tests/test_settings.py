#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.home import Home


class TestSettings:

    @pytest.mark.xfail(reason="Bug 925511 - Unable to log in on dev and stage")
    @pytest.mark.credentials
    def test_email_settings(self, mozwebqa):
        home_page = Home(mozwebqa)

        Assert.false(home_page.is_user_loggedin)
        home_page.login()
        Assert.true(home_page.is_user_loggedin)

        settings_page = home_page.header.click_settings()
        report_inital_state = settings_page.is_report_checked
        events_inital_state = settings_page.is_events_checked

        settings_page.click_report_checkbox()
        settings_page.click_events_checkbox()

        dashboard_page = settings_page.click_save()
        Assert.true(dashboard_page.is_success_message_visible)

        settings_page = home_page.header.click_settings()

        Assert.not_equal(report_inital_state, settings_page.is_report_checked)
        Assert.not_equal(events_inital_state, settings_page.is_events_checked)
