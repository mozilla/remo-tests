#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.link_crawler import LinkCrawler


class TestLabsPage:

    @pytest.mark.skip_selenium
    @pytest.mark.nondestructive
    def test_that_links_in_the_labs_page_return_200_code(self, mozwebqa):
        crawler = LinkCrawler(mozwebqa)
        urls = crawler.collect_links('/labs/', id='wrapper')

        Assert.greater( len(urls), 0,
            'The link crawler did not find any urls to crawl')

        all_ok, bad_urls  = crawler.verify_status_codes_are_ok(urls)
        Assert.true(all_ok, '%s bad links found. ' % len(bad_urls) + ', '.join(bad_urls))
