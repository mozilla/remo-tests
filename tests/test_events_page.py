#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import requests
from icalendar import Calendar
from unittestzero import Assert

from pages.home import Home
from pages.link_crawler import LinkCrawler


class TestEventsPage:

    @pytest.mark.nondestructive
    def test_events_map_is_visible(self, mozwebqa):
        home_page = Home(mozwebqa)

        events_page = home_page.header.click_events_link()
        Assert.true(events_page.is_events_map_visible)

    @pytest.mark.nondestructive
    def test_events_timeline_is_visible(self, mozwebqa):
        home_page = Home(mozwebqa)

        events_page = home_page.header.click_events_link()
        events_page.click_timeline()
        events_page.wait_for_page_to_load()
        Assert.true(events_page.is_events_timeline_visible)

    @pytest.mark.nondestructive
    def test_events_table_is_visible(self, mozwebqa):
        home_page = Home(mozwebqa)

        events_page = home_page.header.click_events_link()
        Assert.true(events_page.is_events_table_visible)

    @pytest.mark.nondestructive
    def test_advanced_options_are_visible(self, mozwebqa):
        home_page = Home(mozwebqa)

        events_page = home_page.header.click_events_link()
        events_page.click_advanced_options()
        Assert.true(events_page.is_advanced_search_form_visible)
        Assert.true(events_page.is_events_icalendar_export_button_visible)

    @pytest.mark.nondestructive
    def test_filter_results_by_owner(self, mozwebqa):
        query = u'John Giannelos'
        home_page = Home(mozwebqa)

        events_page = home_page.header.click_events_link()
        events_page.filter_for(query)
        Assert.equal(u'John Giannelos', events_page.event_profile_owner_text)

    @pytest.mark.nondestructive
    def test_filter_results_by_location(self, mozwebqa):
        query = u'Greece'
        home_page = Home(mozwebqa)

        events_page = home_page.header.click_events_link()
        events_page.filter_for(query)
        Assert.contains(u'Greece', events_page.event_profile_location_text)

    @pytest.mark.skip_selenium
    @pytest.mark.nondestructive
    def test_that_links_in_the_events_page_return_200_code(self, mozwebqa):
        crawler = LinkCrawler(mozwebqa)
        urls = crawler.collect_links('/events/')

        Assert.greater(len(urls), 0,
            'The link crawler did not find any urls to crawl')

        all_ok, bad_urls = crawler.verify_status_codes_are_ok(urls)
        Assert.true(all_ok, '%s bad links found. ' % len(bad_urls) + ', '.join(bad_urls))

    @pytest.mark.nondestructive
    @pytest.mark.xfail('"-dev.allizom" in config.getvalue("base_url")',
                       reason='Bug 967392 - [dev] Discrepancies between the number of event displayed'
                              ' on the site and the ones present in the ICAL export')
    def test_events_icalendar_export(self, mozwebqa):
        home_page = Home(mozwebqa)

        events_page = home_page.header.click_events_link()
        response = requests.get(events_page.events_icalendar_export_button_url, verify=False)

        icalendar = Calendar.from_ical(response.text)
        icalendar_events_count = len(filter(lambda c: c.name == 'VEVENT', icalendar.walk()))

        Assert.equal(icalendar_events_count, events_page.event_items_count)
