"""Tfiac API."""
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pytfiac",
    version="0.0.1alpha",
    author="Fredrik Erlandsson, Pablo Mellado",
    author_email="fredrik.e@gmail.com",
    description="API for Tfiac AC",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fredrike/pytfiac",
    packages=['pytfiac'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPLv3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'xmltodict',
    ],
)
