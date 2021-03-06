# """A setuptools based setup module.
# See:
# https://packaging.python.org/en/latest/distributing.html
# https://github.com/pypa/sampleproject
# """
# # Always prefer setuptools over distutils
# from setuptools import setup, find_packages 
# # To use a consistent encoding
# from codecs import open
# from os import path
# here = path.abspath(path.dirname(__file__))
# # Get the long description from the README file
# with open(path.join(here, 'README.md'), encoding='utf-8') as f:
#     long_description = f.read()
#     setup(
#         name='SAILnet',
#         description='SAILnet algorithm with extensions.',
#         long_description=long_description,
#         )
# """
# # To provide executable scripts, use entry points in preference to the
# # "scripts" keyword. Entry points provide cross-platform support and allow
# # pip to create the appropriate form of executable for the target platform.
# entry_points={
# 'console_scripts': [
# 'ecog=bin:main',
# ],
# },
# """
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sailnet-ligeralde", # Replace with your own username
    version="0.0.1",
    author="Andrew Ligeralde",
    author_email="ligeralde@berkeley.edu",
    description="SAILnet implementation modified from Dodds (2015).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ligeralde/sailnet",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)