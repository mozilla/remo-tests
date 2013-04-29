#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.home import Home
from pages.faq import FAQ
from pages.link_crawler import LinkCrawler


class TestFAQPage:

    @pytest.mark.nondestructive
    def test_faq_sidebar(self, mozwebqa):
        home = Home(mozwebqa)
        home.go_to_homepage()
        faq = home.header.click_faq_link()
        Assert.true(faq.is_faq_sidebar_visible)

    @pytest.mark.skip_selenium
    @pytest.mark.nondestructive
    def test_that_links_in_the_faq_page_return_200_code(self, mozwebqa):
        crawler = LinkCrawler(mozwebqa)
        urls = crawler.collect_links('/faq/', id='wrapper')
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
