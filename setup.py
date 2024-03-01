from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(
    name="kitsai",
    version="0.0.2",
    author="Blaise",
    author_email="iahispano0@gmail.com",
    description="Unofficial package to easily interact with the Kits.AI API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="Attribution-NonCommercial 4.0 International",
    packages=find_packages(),
    url="https://github.com/blaise-tk/kitsai",
    keywords=["python", "audio", "vc", "ai", "rvc", "kits"],
    classifiers=[
        "Development Status :: Release",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: POSIX :: Linux",
    ],
)
