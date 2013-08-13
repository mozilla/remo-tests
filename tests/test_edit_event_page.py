#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import time 
from unittestzero import Assert

from pages.edit_event import EditEvent
from pages.event_detail import EventDetail
from pages.events import Events
from pages.home import Home


class TestEditEventPage:

    @pytest.mark.nondestructive
    def test_edit_event(self, mozwebqa):
        home_page = Home(mozwebqa)
        home_page.login()
        events_page = Events(mozwebqa)
        events_page.go_to_event_detail_page()
        event_detail_page = EventDetail(mozwebqa)
        event_detail_page.click_edit_event_button()
        current_time = str(time.time()).split('.')[0]

        #update event description
        edit_event_page = EditEvent(mozwebqa)
        new_description = "Updated event description %s" % current_time
        edit_event_page.edit_event_description(new_description)
        edit_event_page.click_save_event_button()
        Assert.true(event_detail_page.event_saved_message)
