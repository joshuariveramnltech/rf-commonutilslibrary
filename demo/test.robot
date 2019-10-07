# Created 08/10/2019 00:58 UTC-8
# Author: Joshua Kim Rivera
# email: joshua.rivera@mnltechnology.com
# Github Repository: https://github.com/joshuariveramnltech/rf-commonutilslibrary
*** Settings ***
Documentation                                               Sample test Crop an Element from a screenshot.
# Import the rf-commonutilslibrary.
Library                                                     CommonUtilsLibrary
Library                                                     Collections

*** Variable ***
&{location}                                                 x=607       y=1288
&{size}                                                     height=124      width=446

*** Test Case ***
# Run this test file using this command. 
# robot -d results test.robot (assuming that you are inside this directory)

Test Captcha Decode
    Log To Console                                          ${location}
    Log To Console                                          ${size}
    Capture Element Screenshot                              test_img.png           ${location}           ${size}                 cropped_image.png