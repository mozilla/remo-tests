#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.about import About


class TestAboutPage:

    @pytest.mark.nondestructive
    def test_about_sidebar_is_visible(self, mozwebqa):
        about_page = About(mozwebqa)
        about_page.go_to_about_page()
        Assert.true(about_page.is_about_sidebar_visible)

    @pytest.mark.nondestructive
    def test_about_page_content(self,mozwebqa):
        title = u'About Mozilla Reps'
        about_page = About(mozwebqa)
        about_page.go_to_about_page()
        Assert.equal(title, about_page.is_about_content_visible)
