#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.home import Home
from pages.faq import FAQ


class TestFAQPage:

    @pytest.mark.nondestructive
    def test_faq_sidebar(self, mozwebqa):
        home = Home(mozwebqa)
        home.go_to_homepage()
        faq = home.header.click_faq_link()
        Assert.true(faq.is_faq_sidebar_visible)
