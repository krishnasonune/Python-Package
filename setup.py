from setuptools import setup, find_packages

VERSION = '0.1.2'
DESCRIPTION = 'My first Python package'



# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="TrackFit",
    version=VERSION,
    author="krishna sonune",
    author_email="krishnasonune87@gmail.com",
    description=DESCRIPTION,
    long_description=long,
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