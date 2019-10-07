 Contributing Guidelines
 ===============
Contributions are welcome and appreciated.  
These guidelines instruct how to submit issues and contribute code to
the `CommonUtilsLibrary project`_.

Submitting issues
=================

Bugs and enhancements are tracked in the `issue tracker`_.
If you are unsure if something is a bug or is a feature worth
implementing, you can first ask on `robotframework-users`_ list. This and
other similar forums, not the issue tracker, are also places where to ask
general questions.

Before submitting a new issue, it is always a good idea to check is the
same bug or enhancement already reported. If it is, please add your
comments to the existing issue instead of creating a new one.

Reporting bugs
--------------

Explain the bug you have encountered so that others can understand it
and preferably also reproduce it. Key things to have in good bug report:

-  Python version information
-  SeleniumLibrary, AppiumLibrary, Appium, Selenium and Robot Framework version
-  Browser type, Device OS Version, Device API version, Device Type(IOS, Android)...
-  Also the driver version, example ChromeDriver version.
-  Steps to reproduce the problem. With more complex problems it is
   often a good idea to create a short, self contained, correct example
   `(SSCCE)`_.
-  Possible error message and traceback.

Notice that all information in the issue tracker is public. Do not
include any confidential information there.

Enhancement requests
====================

Describe the new feature and use cases for it in as much detail as
possible in an issue. Especially with larger enhancements, be prepared to
contribute the code in form of a pull request as explained below or to
pay someone for the work. Consider also would it be better to implement this
functionality as a separate library outside the CommonUtilsLibrary.

Choosing something to work on
-----------------------------

Often you already have a bug or an enhancement you want to work on in
your mind, but you can also look at the `issue tracker`_ to find bugs and
enhancements submitted by others. The issues vary significantly in complexity
and difficulty, so you can try to find something that matches your skill
level and knowledge.

Coding conventions
------------------

SeleniumLibrary uses the general Python code conventions defined in
`PEP-8`_. In addition to that, we try to write `idiomatic Python`_
and follow the `SOLID principles`_. with all new code. An important guideline
is that the code should be clear enough that comments are generally not needed.

Docstrings should be added to public keywords but are not generally
needed in internal code. When docstrings are added, they should follow
`PEP-257`_. See `Documentation`_ section below for more details about
documentation syntax, generating docs, etc.

We are pretty picky about using whitespace. We use blank lines and
whitespace in expressions as dictated by
`PEP-8`_, but we also follow these rules:

-  Indentation using tabs, not spaces.
-  No trailing spaces.
-  No extra empty lines at the end of the file.
-  Files must end with a newline.

The above rules are good with most other code too. Any good editor or
IDE can be configured to automatically format files according to them.