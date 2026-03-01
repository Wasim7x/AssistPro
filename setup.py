from setuptools import find_packages,setup

setup(name="assistPro",
       version="0.0.1",
       author="wasim",
       author_email="wasim7x@gmail.com",
       packages=find_packages(),
       install_requires=['langchain-astradb','langchain'])