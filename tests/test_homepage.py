#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import requests
from unittestzero import Assert
from urlparse import urlparse

from pages.home import Home
from pages.link_crawler import LinkCrawler


class TestHomePage:

    _menu_items = ['Main', 'People', 'Events', 'Planet', 'Wiki', 'Labs', 'FAQ']

    @pytest.mark.nondestructive
    def test_menu_items(self, mozwebqa):

        home = Home(mozwebqa)

        home.go_to_homepage()

        for menu_item in home.header.main_menu:
            Assert.contains(menu_item.text, self._menu_items)

    @pytest.mark.skip_selenium
    @pytest.mark.nondestructive
    def test_that_links_in_the_about_page_return_200_code(self, mozwebqa):

        crawler = LinkCrawler(mozwebqa)
        urls = crawler.collect_links('/', id='wrapper')
        bad_urls = []

        Assert.greater(
            len(urls), 0, u'something went wrong. no links found.')

        for url in urls:
            check_result = crawler.verify_status_code_is_ok(url)
            if check_result is not True:
                bad_urls.append(check_result)

        Assert.equal(
            0, len(bad_urls),
            u'%s bad links found. ' % len(bad_urls) + ', '.join(bad_urls))

    @pytest.mark.skip_selenium
    @pytest.mark.nondestructive
    def test_favicon_exists(self, mozwebqa):

        home = Home(mozwebqa)
        favicon_url = home.get_favicon_url
        r = requests.get(favicon_url, verify=False)

        Assert.equal(
            r.status_code, 200,
            u'request to %s responded with %s status code' % (favicon_url, r.status_code))
