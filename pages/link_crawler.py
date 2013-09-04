#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import requests
import threading
import re
from bs4 import BeautifulSoup as soup

from pages.page import Page


class LinkCrawler(Page):

    def collect_links(self, url, **kwargs):
        #check if url is relative
        if url.startswith('/'):
            url = self.base_url + url
        #we only want links that begin with / or http
        link_regex = re.compile('^http|/')
        attrs = {'href': link_regex}
        response = requests.get(url, verify=False)
        html = soup(response.content)
        if kwargs:
            links = [anchor['href'] for anchor in html.find(attrs=kwargs).findAll('a', attrs)]
        else:
            links = [anchor['href'] for anchor in html.findAll('a', attrs)]
        absolute_links = map(
            lambda u:
            u if u.startswith('http')
            else '%s%s' % (self.base_url, u), links)
        return absolute_links

    def verify_status_code_is_ok(self, url):
        if not self.should_verify_url(url):
            return True
        requests.adapters.DEFAULT_RETRIES = 5
        try:
            r = requests.get(url, verify=False, allow_redirects=True, timeout=20)
            status_code = r.status_code
            reason = r.reason
        except requests.Timeout:
            status_code = 408
            reason = 'Connection timed out.'
        if not status_code == requests.codes.ok:
            return u'%s returned: %s - %s' % (url, status_code, reason)
        else:
            return True

    def should_verify_url(self, url):
        """Return false if the url does not need to be verified."""
        bad_urls = ['%s/' % self.base_url, '%s#' % self.base_url]
        return not (url.startswith('%sjavascript' % self.base_url) or
                    url.startswith('%sftp://' % self.base_url) or
                    url.startswith('%sirc://' % self.base_url) or
                    url in bad_urls)

    def verify_status_codes_are_ok(self, urls):
        ''' should use a queue to limit concurrency '''
        results = []
        ''' remove duplicates '''
        urls = list(set(urls))

        def task_wrapper(url):
            checkresult = self.verify_status_code_is_ok(url)
            if checkresult is not True:
                results.append(checkresult)

        threads = [threading.Thread(target=task_wrapper, args=(url,)) for url in urls]
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        return (len(results) == 0, results)
