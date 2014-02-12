ReMo Tests
=========

Automated tests for the ReMo website, reps-dev.allizom.org. Thank you for checking out Mozilla's ReMo test suite. Mozilla and the WebQA team are grateful for the help and hard work of many contributors like yourself. The following contributors have submitted pull requests to the ReMo-Tests project:

https://github.com/mozilla/remo-tests/contributors

Getting involved as a contributor
------------------------------------------

We love working with contributors to fill out the Selenium test coverage for ReMo-Tests, but it does require a few skills.   You will need to know some Python, some Selenium and you will need some basic familiarity with Github.

If you know some Python, it's worth having a look at the Selenium framework to understand the basic concepts of browser based testing and especially page objects. Our suite uses [Selenium WebDriver][webdriver].

If you need to brush up on programming but are eager to start contributing immediately, please consider helping us find bugs in Mozilla [Firefox][firefox] or find bugs in the Mozilla web-sites tested by the [WebQA][webqa] team.

To brush up on Python skills before engaging with us, [Dive Into Python][dive] is an excellent resource.  MIT also has [lecture notes on Python][mit] available through their open courseware.The programming concepts you will need to know include functions, working with classes, and some object oriented programming basics.

[mit]: http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-189-a-gentle-introduction-to-programming-using-python-january-iap-2011/
[dive]: http://www.diveintopython.net/toc/index.html
[webqa]: http://quality.mozilla.org/teams/web-qa/
[firefox]: http://quality.mozilla.org/teams/desktop-firefox/
[webdriver]: http://seleniumhq.org/docs/03_webdriver.html

Questions are always welcome
----------------------------
While we take pains to keep our documentation updated, the best source of information is those of us who work on the project.  Don't be afraid to join us in irc.mozilla.org #mozwebqa to ask questions about our Selenium tests.  Mozilla also hosts the #mozillians chat room to answer your general questions about contributing to Mozilla.

[mozwebqa]:http://02.chat.mibbit.com/?server=irc.mozilla.org&channel=#mozwebqa
[remo]:http://02.chat.mibbit.com/?server=irc.mozilla.org&channel=#remo


Running Tests
-------------
Mozilla maintains a guide to running Automated tests on our QMO website:

https://quality.mozilla.org/docs/webqa/running-webqa-automated-tests/

This wiki page has some advanced instructions specific to Windows:

https://wiki.mozilla.org/QA_SoftVision_Team/WebQA_Automation


### Python
Before you will be able to run these tests, you will need to have Python 2.6 installed.

Run

    easy_install pip

followed by

    sudo pip install -r requirements.txt

__note__

If you are running on Ubuntu/Debian, you will need to do following first:

    sudo apt-get install python-setuptools
    
to install the required Python libraries.

### Running tests locally

To run tests locally, it's a simple case of calling the command below from this directory

    py.test --driver=firefox

For more command line options, see https://github.com/davehunt/pytest-mozwebqa

__note__

To run tests which require user login:

1. Obtain credentials for a test user from [personatestuser][testuser]
2. Create a test user profile on the [mozillians-dev][mozillians] website
3. Join #mozwebqa and ask for getting the testuser profile vouched
4. Specify the path to credentials file like:

        py.test --driver=firefox --credentials=./credentials.yaml tests/test_login_logout.py 

[testuser]:http://personatestuser.org/
[mozillians]:https://mozillians-dev.allizom.org/en-US/


Writing Tests
-------------

If you want to get involved and add more tests, there are just a few things
we'd like to ask you to do:

1. Use the [template files][GitHub Templates] for all new tests and page objects
2. Follow our simple [style guide][Style Guide]
3. Fork this project with your own GitHub account
4. Make sure all tests are passing, and submit a pull request with your changes

[GitHub Templates]: https://github.com/mozilla/mozwebqa-test-templates
[Style Guide]: https://wiki.mozilla.org/QA/Execution/Web_Testing/Docs/Automation/StyleGuide


Pull Requests
---------------------
Submit your pull request to us via GitHub, marking it with a reference to the Git issue or MozTrap test case to give us context to the code.

Contacting us
--------------------
You can find us and other Mozillians that can help out in #mozwebqa on the irc.mozilla.org network. We work primarily across PST and EU timezones.
Feel free to contact us with any queries you may have. We're here to help with problems of any nature.

License
-------
This software is licensed under the [MPL] 2.0:

    This Source Code Form is subject to the terms of the Mozilla Public
    License, v. 2.0. If a copy of the MPL was not distributed with this
    file, You can obtain one at http://mozilla.org/MPL/2.0/.

[MPL]: http://www.mozilla.org/MPL/2.0/
