# -*- coding: utf-8 -*-
from setuptools import setup
from pymaging_png import __version__

setup(
    name = "pymaging-png",
    version = __version__,
    packages = ['pymaging_png'],
    install_requires = ['pymaging'],
    entry_points = {'pymaging.formats': ['png = pymaging_png.png:PNG']},
    author = "Jonas Obrist",
    author_email = "ojiidotch@gmail.com",
    description = "PNG support for Pymaging",
    license = "BSD",
    keywords = "pymaging png imaging",
    url = "https://github.com/ojii/pymaging-png/",
    zip_safe = False,
    test_suite = 'pymaging_png.tests'
)
