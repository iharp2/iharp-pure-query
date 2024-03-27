"""
Query Functions
===============

All queries should return result as xarray.DataArray.
"""

import xarray


def time_series_query(
    variable: str,
    min_lat: float,
    max_lat: float,
    min_lon: float,
    max_lon: float,
    start_datetime: str,
    end_datetime: str,
    time_resolution: str,
    aggregation_method: str,
) -> xarray.DataArray:
    """
    "have a time series of a certain variable V over area A and time period T"
    E.g., "draw the average temperature heatmap of Greenland over the last year."
    """
    # TODO: Implement this function
    return xarray.DataArray()


def heat_map_query(
    variable: str,
    min_lat: float,
    max_lat: float,
    min_lon: float,
    max_lon: float,
    start_datetime: str,
    end_datetime: str,
    aggregation_method: str,
) -> xarray.DataArray:
    """
    "have the heatmap of a certain variable V over a certain area A and certain time period T"
    E.g., "draw the average temperature heatmap of Green- land over the last year."
    """
    # TODO: Implement this function
    return xarray.DataArray()


def value_predicate_query(
    variable: str,
    min_lat: float,
    max_lat: float,
    min_lon: float,
    max_lon: float,
    start_datetime: str,
    end_datetime: str,
    predicate_verb: str,  # e.g., "=", ">", "<", ">=", "<=", "!="
    predicate_value: float,
) -> xarray.DataArray:
    """
    "retrieve records based on a certain variable criteria"
    E.g., "find all data records in the world over the last year where the temperature has exceeded 240."
    """
    # TODO: Implement this function
    return xarray.DataArray()


def arbitrary_shape_query(
    variable: str,
    shape: str,
    start_datetime: str,
    end_datetime: str,
) -> xarray.DataArray:
    """
    "retrieve records within an arbitrary shape"
    E.g., "find all data records in Greenland over the last year."
    """
    # TODO: Implement this function
    return xarray.DataArray()
