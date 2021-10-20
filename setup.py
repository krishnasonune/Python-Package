from setuptools import setup, find_packages

VERSION = '0.0.7'
DESCRIPTION = 'My first Python package'
LONG_DESCRIPTION = 'This package will help to calculate calories to achieve your goal faster ' \
"""


        
            from TrackFit import musclegain
            
            from TrackFit import maintenance
            
            from TrackFit import bodyrecomposition
            
            from TrackFit import fatloss






"""

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="TrackFit",
    version=VERSION,
    author="krishna sonune",
    author_email="krishnasonune87@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'first package'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]

)