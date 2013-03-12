#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.home import Home
from pages.events import Events


class TestEventsPage:

    @pytest.mark.nondestructive
    def test_events_map(self, mozwebqa):
        home = Home(mozwebqa)
        home.go_to_homepage()
        events = home.header.click_events_link()
        Assert.true(events.is_events_map_visible)
