#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.events import Events
from pages.link_crawler import LinkCrawler


class TestEventsPage:

    @pytest.mark.nondestructive
    def test_events_map_is_visible(self, mozwebqa):
        events_page = Events(mozwebqa)
        events_page.go_to_events_page()
        Assert.true(events_page.is_events_map_visible)

    @pytest.mark.nondestructive
    def test_events_table_is_visible(self, mozwebqa):
        events_page = Events(mozwebqa)
        events_page.go_to_events_page()
        Assert.true(events_page.is_events_table_visible)

    @pytest.mark.nondestructive
    def test_filter_results_by_owner(self, mozwebqa):
        query = u'John Giannelos'
        events_page = Events(mozwebqa)
        events_page.go_to_events_page()
        events_page.filter_for(query)
        Assert.equal(u'John Giannelos', events_page.event_profile_owner_text)

    @pytest.mark.nondestructive
    def test_filter_results_by_location(self, mozwebqa):
        query = u'Greece'
        events_page = Events(mozwebqa)
        events_page.go_to_events_page()
        events_page.filter_for(query)
        Assert.contains(u'Greece', events_page.event_profile_location_text)

    @pytest.mark.skip_selenium
    @pytest.mark.nondestructive
    def test_that_links_in_the_events_page_return_200_code(self, mozwebqa):
        crawler = LinkCrawler(mozwebqa)
        urls = crawler.collect_links('/events/', id='wrapper')
        bad_urls = []

        Assert.greater(
            len(urls), 0,
            'The link crawler did not find any urls to crawl')

        for url in urls:
            check_result = crawler.verify_status_code_is_ok(url)
            if check_result is not True:
                bad_urls.append(check_result)

        Assert.equal(
            0, len(bad_urls),
            '%s bad links found. ' % len(bad_urls) + ', '.join(bad_urls))
