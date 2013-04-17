#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.people import People


class TestPeoplePage:

    @pytest.mark.nondestructive
    def test_people_map_is_visible(self, mozwebqa):
        people_page = People(mozwebqa)
        people_page.go_to_people_page()
        Assert.true(people_page.is_people_map_visible)

    @pytest.mark.nondestructive
    def test_profile_grid_is_visible(self, mozwebqa):
        people_page = People(mozwebqa)
        people_page.go_to_people_page()
        Assert.true(people_page.is_profile_grid_visible)
        Assert.true(people_page.is_profile_name_visible)
        Assert.true(people_page.is_profile_image_visible)
