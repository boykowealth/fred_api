from setuptools import setup, find_packages

setup(
    name="fred_api",
    version="1.0",
    packages=find_packages(),
    install_requires=["pandas"],
    author="Brayden Boyko",
    description="This Python module provides a simple interface to fetch and parse economic data series from the Federal Reserve Economic Data (FRED) API. Using this module, you can retrieve time series data from FRED, including economic indicators, inflation rates, and other key datasets.",
    url="https://github.com/boykowealth/fred_api",
)