import setuptools
import os

_here = os.path.abspath(os.path.dirname(__file__))

with open("README.md", "r") as fh:
    long_description = fh.read()

version = {}
with open(os.path.join(_here, 'nice_figures', 'version.py')) as f:
    exec(f.read(), version)

setuptools.setup(
    name="nice-figures",
    version=version['__version__'],
    author="Rob Bettles",
    author_email="rjbcoding@gmail.com",
    description="Methods and style files for making publication quality figures",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Rob217/nice-figures",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
      'matplotlib'
    ],
    python_requires='>=3.6',
    include_package_data=True,
    package_data={'' : [os.path.join('data', '*.json')]},
)
