import pytest
import pandas as pd
from extract_data import skapa_dataframe, hämta_väderdata

# ------------------ Test hämta_väderdata ------------------
def test_hämta_väderdata_returns_dict():
    data = hämta_väderdata("göteborg")
    assert isinstance(data, dict)
    assert "timeSeries" in data

def test_hämta_väderdata_invalid_city():
    import pytest
    with pytest.raises(ValueError):
        hämta_väderdata("invalid_city")

# ------------------ Test skapa_dataframe ------------------
def test_skapa_dataframe_returns_dataframe():
    df = skapa_dataframe("göteborg")
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert "tid" in df.columns
    assert "grad" in df.columns

def test_skapa_dataframe_first_24_rows():
    df = skapa_dataframe("göteborg")
    # Should return max 24 rows
    assert len(df) <= 24