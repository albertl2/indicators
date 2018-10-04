import pytest
import math
from movingaverage import MovingAverage

@pytest.fixture
def timeseries():
    import pandas as pd
    df = pd.read_csv('test/MMM_2006_01_01_to_2017_12_29.csv')
    df = df.fillna('')
    # df = df.head(1000)
    return df

@pytest.fixture
def ts_original(timeseries):
    return timeseries['original'].tolist()

@pytest.fixture
def ts_ma_5(timeseries):
    return timeseries['MA-5'].tolist()

@pytest.fixture
def ts_ma_12(timeseries):
    return timeseries['MA-12'].tolist()

@pytest.fixture
def ts_ma_50(timeseries):
    return timeseries['MA-50'].tolist()

# Check that kwargs are honored.
def test_ma_kwargs_period_5():
    indic = MovingAverage([1,2,3],period=5)
    assert indic.period == 5

def test_ma_kwargs_period_12():
    indic = MovingAverage([1,2,3],period=12)
    assert indic.period == 12

def test_ma_kwargs_period_50():
    indic = MovingAverage([1,2,3],period=50)
    assert indic.period == 50

# Output, n=5.
def test_ma_output_n_5(ts_original,ts_ma_5):
    indic = MovingAverage(ts_original,period=5)
    for od,ad in zip(indic.od[indic.period-1:-1],ts_ma_5[indic.period-1:-1]):
        assert math.isclose(od,ad,rel_tol=1e-3)

# Output, n=12.
def test_ma_output_n_12(ts_original,ts_ma_12):
    indic = MovingAverage(ts_original,period=12)
    for od,ad in zip(indic.od[indic.period:-1],ts_ma_12[indic.period:-1]):
        assert math.isclose(od,ad)

# Output, n=50.
def test_ma_output_n_50(ts_original,ts_ma_50):
    indic = MovingAverage(ts_original,period=50)
    for od,ad in zip(indic.od[indic.period:-1],ts_ma_50[indic.period:-1]):
        assert math.isclose(od,ad)
