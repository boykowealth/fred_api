
# FRED API Data Retrieval

This Python module provides a simple interface to fetch and parse economic data series from the Federal Reserve Economic Data (FRED) API. Using this module, you can retrieve time series data from FRED, including economic indicators, inflation rates, and other key datasets.

## Features

- Retrieves time series data from the FRED API.
- Allows filtering by date range.
- Supports proxies for network connections.
- Cleans and formats data for easy analysis.

## Installation

1. Ensure you have Python 3.x installed.
2. Install the required packages using pip:
   ```bash
   pip install pandas
   ```

## Usage

The module contains a `FRED` class with methods to fetch and format time series data from the FRED API.

```python
from fred_data import FRED

# Initialize with your FRED API key
fred = FRED(api_key='YOUR_API_KEY')

# Fetch data for a specific FRED series
data = fred.get_series(series_id='CPIAUCSL', observation_start='2020-01-01', observation_end='2023-01-01')
print(data.head())
```

## Code Overview

### `FRED` Class

- **`__init__()`**: Initializes the FRED API client with an API key. You can provide the API key directly, through a file, or by setting an environment variable (`FRED_API_KEY`).
- **`__fetch_data()`**: Internal method to handle the API call and parse XML responses.
- **`get_series()`**: Main method to retrieve data for a specified series, with optional date filtering.

### `data` Method

This method simplifies the process of creating a DataFrame from a FRED series.

```python
# Fetch and display the cleaned data as a DataFrame
fred = FRED(api_key='YOUR_API_KEY')
series_data = fred.data(api='YOUR_API_KEY', series_id='CPIAUCSL', observation_start='2020-01-01', observation_end='2023-01-01')
print(series_data.head())
```

### Sample Output

```
| DATE       | CPIAUCSL |
|------------|----------|
| 2020-01-01 | 258.678  |
| 2020-02-01 | 259.105  |
| 2020-03-01 | 259.829  |
| ...        | ...      |
```

## How Boyko Wealth Uses This Data

At **Boyko Wealth**, this FRED data integration helps in creating economic and market models by providing reliable historical data on macroeconomic indicators, employment rates, inflation, and interest rates. These insights are essential for:

- **Economic Forecasting**: Modeling economic scenarios based on historical trends.
- **Inflation Analysis**: Tracking Consumer Price Index (CPI) and other inflation metrics to gauge purchasing power and cost-of-living changes.
- **Investment Strategy**: Incorporating economic indicators into models for evaluating market conditions and refining portfolio allocation.

By utilizing the FRED API, Boyko Wealth leverages high-quality economic data to provide deeper market insights and enhance data-driven wealth management strategies for our clients.

## Requirements

- **pandas**: For data manipulation.
- **xml.etree.ElementTree**: For parsing XML responses from the FRED API.
