#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert
from pages.home import Home

class TestHomePage:

    _menu_items = ['Main', 'People', 'Events', 'Planet', 'Wiki', 'Labs', 'FAQ']

    @pytest.mark.nondestructive
    def test_menu_items(self, mozwebqa):

        home = Home(mozwebqa)

        home.go_to_homepage()

        for menu_item in home.header.main_menu:
            Assert.contains(menu_item.text, self._menu_items)
