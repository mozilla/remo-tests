#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.home import Home


class TestSettings:

    @pytest.mark.credentials
    def test_email_settings(self, mozwebqa):
        home = Home(mozwebqa)
        home.go_to_homepage()
        Assert.false(home.is_user_loggedin)
        home.login()
        Assert.true(home.is_user_loggedin)

        settings = home.header.click_settings()
        report_inital_state = settings.is_report_checked
        events_inital_state = settings.is_events_checked

        settings.click_report_checkbox()
        settings.click_events_checkbox()

        settings.click_save()

        settings = home.header.click_settings()

        Assert.not_equal(report_inital_state, settings.is_report_checked)
        Assert.not_equal(events_inital_state, settings.is_events_checked)
