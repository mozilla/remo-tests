#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert
from pages.link_crawler import LinkCrawler

from pages.people import People
from pages.profile import Profile


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

    @pytest.mark.nondestructive
    def test_people_page_links(self, mozwebqa):
        crawler = LinkCrawler(mozwebqa)
        urls = crawler.collect_links('/people', id ='wrapper')
        bad_urls = []

        Assert.greater(len(urls), 0, u'something went wrong. no links found.')

        for url in urls:
            check_result = crawler.verify_status_code_is_ok(url)
            if check_result is not True:
                bad_urls.append(check_result)

        Assert.equal(
            0, len(bad_urls),
            u'%s bad links found. ' % len(bad_urls) + ', '.join(bad_urls))

    @pytest.mark.nondestructive
    def test_filter_results_by_name(self, mozwebqa):
        query = u'Billings'
        people_page = People(mozwebqa)
        people_page.go_to_people_page()
        people_page.filter_for(query)
        Assert.equal(u'Billings', people_page.is_people_name_text_visible)

        #Check profile to verify search results where name is not visible
        query = u'John'
        people_page = People(mozwebqa)
        people_page.go_to_people_page()
        people_page.filter_for(query)
        people_page.click_to_open_profile()
        profile_page = Profile(mozwebqa)
        Assert.true(profile_page.is_text_present(query))
