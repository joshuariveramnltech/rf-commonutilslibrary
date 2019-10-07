from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
      name='rf-commonutilslibrary',
      version='0.1dev',
      description='A compiled keyword utilities for running test with rf-seleniumlibrary or rf-appiumlibrary.',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/joshuariveramnltech/rf-commonutilslibrary',
      author='Joshua Kim Rivera, Shiela M. Buitizon',
      author_email='joshua.rivera@mnltechnology.com, shiela.buitizon@mnltechnology.com',
      packages= ['CommonUtilsLibrary'],
)