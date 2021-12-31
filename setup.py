
from setuptools import setup, find_packages
import sys

VERSION = '0.1.0'
DESCRIPTION = 'UMNSVP package for outputting dict to terminal.'
LONG_DESCRIPTION = """"""

requirements = ["mypy"]
platform = sys.platform
if "NT" in platform or "Windows" in platform:
    requirements.append("windows-curses")

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="livedict",
    version=VERSION,
    author="Jacob Bunzel <bunze002@umn.edu",
    author_email="bunze002@umn.edu",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=requirements,

    keywords=['python', 'CAN', "curses"]
)
