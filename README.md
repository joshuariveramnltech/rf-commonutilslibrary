Robotframework - CommonUtilsLibrary
================

## Introduction  
CommonUtilsLibrary is a Testing Library for RobotFramework.

It uses Python Libraries to perform its keyword operations.

It is written in Python 3.x.

## Documentation  
The Keyword documentation is currently unavailable right now, but will be posted the moment it is available.


## Installation
* Install using pip:
  * This is the recommended installtion method.  
    *  Step 1: Clone this repository.
    *  Step 2: From the root of this repository, run `pip install .`
  
 * Using setup.py:
   * setup.py
     * Step 1: Clone this repository
     * Step 2: from the root of this repository, run `python setup.py install`   


Validate Successful Installation by running `pip freeze`, the package should now be listed among the list of packages if the installtion is successful.


## Usage:
To write test using this Library, CommonUtilsLibrary should first be imported in your RF test suite.
```robotframework
*** Setting ***
Documentation                                       This is a sample test suite.

Library                                             CommonUtilsLibrary


*** Variables ***
${your_sample_variable}                             Sample String Variable


*** Keywords ***
Sample Keyword
    Sample Keyword From the CommonUtilsLibrary


*** Test Cases ***
Sample Test Case
    Sample Keyword
```

## Contributing:
Contributions are welcome. To start contributing, please read out CONTRIBUTING guide.


## Contributors
* Joshua Kim Rivera - email: joshua.rivera@mnltechnology.com