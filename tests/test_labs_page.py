#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.home import Home
from pages.labs import Labs


class TestLabsPage:

    @pytest.mark.nondestructive
    def test_labs_sidebar(self, mozwebqa):
        home_page = Home(mozwebqa)
        home_page.go_to_homepage()
        faq = home_page.main_menu.click_labs_link()
        Assert.true(labs.is_the_current_page)
