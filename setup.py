from setuptools import setup, find_packages

requirements : list = ["pycryptodome" , "pillow" , "aiohttp" , "websocket-client"]

setup(
    name = "rubi",
    version = "2.5.0",
    author = "Reza Khodayi",
    author_email = "snipe4kill.tg@gmail.com",
    description = "This is an unofficial library for deploying robots on Rubika accounts.",
    long_description = "Loading...",
    long_description_content_type = "text/markdown",
    url = "https://github.com/snipe4kill/rubpy/",
    packages = find_packages(),
    install_requires = requirements,
    classifiers = [
    	"Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
    ],
)