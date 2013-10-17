#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.home import Home


class TestLogInOut:

    @pytest.mark.credentials
    @pytest.mark.nondestructive
    def test_login_logout(self, mozwebqa):
        home_page = Home(mozwebqa)

        Assert.false(home_page.is_user_loggedin)
        home_page.login()
        Assert.true(home_page.is_user_loggedin)

        # log out after logging in
        home_page.click_logout_menu_item()
        Assert.false(home_page.is_user_loggedin)
