#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import requests
from unittestzero import Assert

from pages.home import Home
from pages.link_crawler import LinkCrawler
from base_test import BaseTest


class TestHomePage(BaseTest):

    _menu_items = ['Main', 'People', 'Events', 'Planet', 'Wiki', 'Labs', 'FAQ']

    @pytest.mark.nondestructive
    def test_menu_items(self, mozwebqa):

        home_page = Home(mozwebqa)

        for menu_item in home_page.header.main_menu:
            Assert.contains(menu_item.text, self._menu_items)

    @pytest.mark.skip_selenium
    @pytest.mark.nondestructive
    def test_that_links_in_the_home_page_return_200_code(self, mozwebqa):
        crawler = LinkCrawler(mozwebqa)
        urls = crawler.collect_links('/')

        Assert.greater(len(urls), 0,
            u'The link crawler did not find any urls to crawl')

        all_ok, bad_urls = crawler.verify_status_codes_are_ok(urls)
        Assert.true(all_ok, '%s bad links found. ' % len(bad_urls) + ', '.join(bad_urls))

    @pytest.mark.nondestructive
    def test_favicon_exists(self, mozwebqa):

        home = Home(mozwebqa)
        favicon_url = home.get_favicon_url
        # get the response code for the favicon_url, converting it into an absolute url
        response_code = self.get_response_code(
            self.make_absolute(favicon_url, mozwebqa.base_url), mozwebqa.timeout
        )
        # check that the response code is ok
        Assert.equal(response_code, requests.codes.ok)
