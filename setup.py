import os
from setuptools import setup

setup(
    name='cocotb-stub-sim',
    packages=['cocotb_stub_sim'],
    package_dir={'' : 'src'},
    author = "Matthew Ballance",
    author_email = "matt.ballance@gmail.com",
    description = "Stub cocotb 'simulator' interface for unit testing",
    long_description="""
    Enables running unit tests without a simulator
    """,
    license = "Apache 2.0",
    keywords = ["SystemVerilog", "Verilog", "RTL", "cocotb", "Python"],
    url = "https://github.com/fvutils/cocotb-stub-sim",
    setup_requires=[
        'setuptools_scm'
    ],
    install_requires=[
        'cocotb'
    ]
    )