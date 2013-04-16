#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.home import Home

class TestLogInOut:

    @pytest.mark.nondestructive
    def test_login_logout(self, mozwebqa):
        home = Home(mozwebqa)
        home.go_to_homepage()
        Assert.false(home.is_user_loggedin)
        home.login()
        Assert.true(home.is_user_loggedin)

        # log out after logging in
        home.click_logout_menu_item()
        Assert.false(home.is_user_loggedin)
