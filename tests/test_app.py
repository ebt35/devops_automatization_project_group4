import os
import sys

# Lägg till projektroten i sys.path så "weather_app" kan importeras
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pytest
import pandas as pd

from weather_app.extract_data import get_weather_data, create_dict


# Unit test
def test_get_weather_data_invalid_city():
    """Ogiltig stad ska ge ValueError utan API-anrop."""
    with pytest.raises(ValueError):
        get_weather_data("invalid_city")


# Integration tests
def test_get_weather_data_returns_dict():
    data = get_weather_data("göteborg")
    assert isinstance(data, dict)
    assert "timeSeries" in data


def test_create_dict_returns_dataframe():
    df = create_dict("göteborg")
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert "time" in df.columns
    assert "degree" in df.columns


def test_create_dict_max_24_rows():
    df = create_dict("göteborg")
    assert len(df) <= 24
