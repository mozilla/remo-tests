#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import random
import string
from copy import deepcopy
from unittestzero import Assert

from pages.home import Home


class TestProfilePage:

    @pytest.mark.credentials
    def test_edit_profile_fields(self, mozwebqa):
        home_page = Home(mozwebqa)
        home_page.login()

        profile_page = home_page.header.click_profile()
        user_edit_page = profile_page.click_edit_profile()
        Assert.true(user_edit_page.is_the_current_page)

        # save initial values to restore them after the test is finished
        fields_no = len(user_edit_page.profile_fields)
        initial_value = [None] * fields_no
        random_name = "test%s" % random.choice(string.lowercase)

        # enter new values
        for i in range(0, fields_no):
            initial_value[i] = deepcopy(user_edit_page.profile_fields[i].field_value)
            user_edit_page.profile_fields[i].clear_field()
            user_edit_page.profile_fields[i].type_value(random_name)

        user_edit_page.click_save_profile()
        Assert.true(profile_page.is_update_message_visible)
        profile_page.click_edit_profile()

        # using try finally to ensure that the initial values are restore even if the Asserts fail.
        try:
            for i in range(0, fields_no):
                Assert.contains(random_name, user_edit_page.profile_fields[i].field_value)

        except Exception as exception:
            Assert.fail(exception)

        finally:
            # go back and restore initial values
            for i in range(0, fields_no):
                user_edit_page.profile_fields[i].clear_field()
                user_edit_page.profile_fields[i].type_value(initial_value[i])

            user_edit_page.click_save_profile()

    @pytest.mark.credentials
    def test_user_can_create_report(self, mozwebqa):
        home_page = Home(mozwebqa)
        home_page.login()

        profile_page = home_page.header.click_profile()

        if profile_page.editable_monthly_reports_present:
            edit_report_page = profile_page.click_random_editable_monthly_reports()
            fields_no = len(edit_report_page.report_fields) - 1
            random_text = "test%s" % random.choice(string.lowercase)

            # enter report values
            for i in range(0, fields_no):
                edit_report_page.report_fields[i].clear_field()
                edit_report_page.report_fields[i].type_value(random_text)

            test_link = 'http://test.com'
            edit_report_page.set_input_text_for('event_link', test_link)
            edit_report_page.set_input_text_for('activity_link', test_link)
            edit_report_page.set_input_text_for('event_name', random_text)
            edit_report_page.set_input_text_for('activity_description', random_text)
            value = '2'
            edit_report_page.select_type_of_participation(value)

            edit_report_page.click_save_report_button()

            Assert.true(edit_report_page.is_success_message_visible)
            Assert.contains('Report successfully created.', edit_report_page.success_message_text)

        else:
            edit_report_page = profile_page.click_random_existing_monthly_reports()
            edit_report_page.click_edit_report_button()
            edit_report_page.delete_report()
            Assert.true(edit_report_page.is_success_message_visible)
            Assert.contains('Report successfully deleted.', edit_report_page.success_message_text)

            profile_page.click_random_editable_monthly_reports()
            fields_no = len(edit_report_page.report_fields) - 1
            random_text = "test%s" % random.choice(string.lowercase)

            # enter report values
            for i in range(0, fields_no):
                edit_report_page.report_fields[i].clear_field()
                edit_report_page.report_fields[i].type_value(random_text)

            test_link = 'http://test.com'
            edit_report_page.set_input_text_for('event_link', test_link)
            edit_report_page.set_input_text_for('activity_link', test_link)
            edit_report_page.set_input_text_for('event_name', random_text)
            edit_report_page.set_input_text_for('activity_description', random_text)
            value = '3'
            edit_report_page.select_type_of_participation(value)

            edit_report_page.click_save_report_button()
            Assert.true(edit_report_page.is_success_message_visible)
            Assert.contains('Report successfully created.', edit_report_page.success_message_text)
