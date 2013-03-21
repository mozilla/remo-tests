#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.events import Events


class TestEventsPage:

    @pytest.mark.nondestructive
    def test_events_map(self, mozwebqa):
        events_page = Events(mozwebqa)
        events_page.go_to_events_page()
        Assert.true(events_page.is_events_map_visible)
