#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from unittestzero import Assert
from pages.not_found import NotFound


class TestNotFoundPage:

    def test_page_not_found(self, mozwebqa):
        not_found = NotFound(mozwebqa)
        not_found.go_to_inexisting_page()
        Assert.true(not_found.is_404_error_message_visible)
        Assert.equal(not_found.get_error_message(), '404 - Not found')



