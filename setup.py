#  Copyright (c) 2020. Vinci Consulting Corp. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="vpppapigen-enumflag",
    version="0.0.0alpha0",
    description="Enumflag emitter plugin for vppapigen.",
    author="Paul Vinciguerra",
    author_email="pvinci@vinciconsulting.com",
    url="https://wiki.fd.io/view/VPP/Python_API",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    license="Apache-2.0",
    test_suite=".",
    packages=find_packages(),
    install_requires=["vppapigen"],
    long_description=long_description,
    entry_points={
        "vppapigen.emitters": "ENUMFLAG = vppapigen_enumflag.vppapigen_enumflag"
    },
    zip_safe=True,
)
