# FRED API Connection Tool
Simple FRED Rest API Connection Tool - Output In Pandas DataFrame.

_Boyko Wealth Utilizes The FRED API For Econnomic Research And Modelling. This Tool Was Designed To Allow Clean Outputs And Fast Connection Speeds. An Offical FRED API Key Is Required For Use._

## The Tool
The tool utilizes the official FRED API root URL (https://api.stlouisfed.org/fred) to manage and store datapoints. To use the tool, utilize the following function: FRED.data(api,series_id, observation_start=None, observation_end=None, **kwargs).
Where:
        api: Official FRED API Key
        series_id: Offical FRED Datapoint ID (ex. SP500 - S&P 500)
        observation_start: Start Date In String Form (ex. "2020-01-01")
        observation_end: End Date In String Form (ex. 2024-01-01)
        **kwargs: Key Filters (ex. frequency='Quarterly')

## The Output
All outputs will return a Pandas DataFrame. This DataFrame will be have two columns, the first column header is called DATE and displays the date in format (YYYY-MM-DD). The second column is the name of your data measure capitalized (ex. SP500). The output looks like this when printed:

---
           DATE    SP500
0    2020-01-01  3251.83
1    2020-01-02  3257.85
2    2020-01-03  3234.85
3    2020-01-06  3246.28
4    2020-01-07  3237.18
...         ...      ...
1253 2024-10-21  5853.98
1254 2024-10-22  5851.20
1255 2024-10-23  5797.42
1256 2024-10-24  5809.86
1257 2024-10-25  5808.12
---

**You Can Get Your Free API Key Here:** https://fredaccount.stlouisfed.org/login/secure/


