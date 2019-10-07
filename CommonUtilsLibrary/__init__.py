""" 
CommonUtilsLibrary
Version = 0.1dev
Library Scope: GLOBAL
Created: 08/10/2019 00:45 UTC-8
Author: Joshua Kim Rivera   | email:joshua.rivera@mnltechnology.com
        Shiela Buitizon     | email:shiela.buitizon@mnltechnology.com 
Company: Spiralworks Technologies Inc.

Description:
    CommonUtilsLibrary is a Testing Library for RobotFramework.
    It uses Python Libraries to perform its keyword operations.

Importing this library in your test suite:
    Sample:
    =============================================================
    || *** Settings ***                                        ||
    || Library                         CommonUtilsLibrary      ||
    ||                                                         ||
    || *** Keywords ***                                        ||
    || your_keywords_here                                      ||
    ||                                                         ||
    ||                                                         ||
    || *** Test Cases ***                                      ||
    || sample_library_keyword_here                             ||
    ||                                                         ||
    =============================================================
Developer Manual:
    Compiling this pip package:
        - python setup.py bdist_wheel
    
    Uploading build to pip
        - python -m twine upload dist/*
"""

from PIL import Image

__version__ = '0.1'

class CommonUtilsLibrary(object):

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def capture_element_screenshot(self, imagepath, location, size, output_path):
        img = Image.open(imagepath)
        x, y, width, height = int(location['x']) , int(location['y']), int(size['width'])+int(location['x']), int(size['height'])+int(location['y'])
        cropped = img.crop((x, y, width, height))
        cropped.save(output_path)