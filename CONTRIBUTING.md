# Introduction

### Welcome to the covid19-data developer community!

First off, thank you for considering contributing to covid19-data. It's people like you that make
covid19-data such a great tool

### Purpose of contributor guidelines

Following these guidelines helps to communicate that you respect the time of the developers managing
and developing this open source project. In return, we will reciprocate that respect in addressing
your issue, assessing changes, and helping you finalize your pull requests

### What kinds of contributions we are looking for

covid19-data is an open source project and we love to receive contributions from our community — you!
There are many ways to contribute, from writing tutorials or blog posts, improving the documentation,
submitting bug reports and feature requests or writing code which can be directly incorporated into
covid19-data

### What contributions are not accepted

Please do not use the issue tracker for support and help related questions. The issue tracker is only for bug reports,
feature requests, and other related topics. For general support and discussion join the official
[Discord server](https://discord.gg/yCDH8c4) or email [admin@bnrydev.co](mailto:admin@bnrydev.co). Also
you may not submit contributions that violate the TOS of our project or that of John Hopkins University,
The COVID Tracking Project, or that of any of the sources listed in the Data Sources section of README.md

# Ground Rules
### Expectations for contributors and developers
You must be respectful to all members of the community, as well as being fully transparent about the
intent and purpose of your contribution. When making a contribution make sure to follow the code of
conduct, to ensure that everyone upholds the standards of the community. Developers in turn agree
to follow guidelines as well, and to take each issue seriously and handle all issues in a professional
manor

Responsibilities
* Ensure cross-platform compatibility for every change that's accepted. Windows, Mac, Debian & Ubuntu Linux
* Ensure that code that goes into core meets all requirements in this
[checklist](https://gist.github.com/audreyr/4feef90445b9680475f2)
* Create issues for any major changes and enhancements that you wish to make. Discuss things transparently and get community feedback
* Don't add any classes to the codebase unless absolutely needed. Err on the side of using functions
* Keep feature versions as small as possible, preferably one new feature per version
* Be welcoming to newcomers and encourage diverse new contributors from all backgrounds. See the
[Python Community Code of Conduct](https://www.python.org/psf/codeofconduct/)

# Your First Contribution
### Resources for first time open source contributors
* Here are a couple of friendly tutorials you can follow: http://makeapullrequest.com/ and http://www.firsttimersonly.com/
* Working on your first Pull Request? You can learn how from this *free* series,
[How to Contribute to an Open Source Project on GitHub](https://egghead.io/series/how-to-contribute-to-an-open-source-project-on-github).
* At this point, you're ready to make your changes! Feel free to ask for help; everyone is a beginner at first
* If a maintainer asks you to "rebase" your PR, they're saying that a lot of code has changed, and that you need to update
 your branch so it's easier to merge.

# Getting started
* To contribute to this project, your code must run all pass all existing tests and you must write tests
to test the validity of your own code
    * To run unit tests run ```pytest``` from the root project directory
    * Your unit tests need to follow the naming scheme of the rest of the project
    * Your code will not be merged into the codebase if any unit tests are failing

* For something that is bigger than a one or two line fix:
    1. Create your own fork of the code
    2. Do the changes in your fork
    3. If you like the change and think the project could use it:
        * Be sure you have followed the code style for the project.
        * Sign the Contributor License Agreement, CLA, with BNRyDev Co.
        * Note the BNRyDev Co. Code of Conduct.
        * Send a pull request indicating that you have a CLA on file.

Small contributions such as fixing spelling errors, where the content is small enough to not be considered
intellectual property, can be submitted by a contributor as a patch, without a CLA.

As a rule of thumb, changes are obvious fixes if they do not introduce any new functionality or
creative thinking. As long as the change does not affect functionality,
some likely examples include the following:
* Spelling / grammar fixes
* Typo correction, white space and formatting changes
* Comment clean up
* Bug fixes that change default return values or error codes stored in constants
* Adding logging messages or debugging output
* Changes to ‘metadata’ files like Gemfile, .gitignore, build scripts, etc.
* Moving source files from one directory or package to another

# How to report a bug
If you find a security vulnerability, do NOT open an issue. Email admin@bnrydev.co instead.

In order to determine whether you are dealing with a security issue, ask yourself these two questions:
* Can I access something that's not mine, or something I shouldn't have access to?
* Can I disable something for other people?

If the answer to either of those two questions are "yes", then you're probably dealing with a security issue.
Note that even if you answer "no" to both questions, you may still be dealing with a security issue,
so if you're unsure, just email us at admin@bnrydev.co

### Standard Bug reporting
Template:

     When filing an issue, make sure to answer these five questions:
     1. What version of Python are you using, and what version of the package is currently installed?
     2. What operating system and processor architecture are you using?
     3. What did you do?
     4. What did you expect to see?
     5. What did you see instead?

# How to suggest a feature or enhancement
### Goals and philosophy of covid19-data
The goal of covid19-data is to provide a python3 library to get COVID-19 statistics and data, with lowest
overhead possible, so that the user does not ever have to worry about performance. Our philosophy is
centered around the idea that the easier the code is to implement and read, the better. Following this
mindset is a crucial part of the development process, and feature and enhancement requests that are
centered around this will be given a much higher priority over other requests.

### Process for suggesting a feature
If you find yourself wishing for a feature that doesn't exist in covid19-data, you are probably not alone.
There are bound to be others out there with similar needs. Many of the features that covid19-data
has today have been added because our users saw the need. Open an issue on our issues list on
GitHub which describes the feature you would like to see, why you need it, and how it should work.

# Code review process
### How contributions become approved once they are sumbitted

The core team looks at Pull Requests on a regular basis in a weekly triage meeting that we hold in a
public discord call. The meeting is announced in the weekly status updates in our developer discord server.
Notes are posted to the contributor notes channel on discord. After feedback has been given we expect
responses within two weeks. After two weeks we may close the pull request if it isn't showing any activity.

# Community
This project is the intellectual property of BNRyDev Co., and is developed by BinaryNightowl. The 
project is currently maintained by BinaryNightowl, gdettling, and irondextros.

[Official Discord Server](https://discord.gg/yCDH8c4)

[Twitter](https://twitter.com/BNRyDevCo)
