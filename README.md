# Indicator Library

Contains a base class contained in `indicator.py`. Each indicator is built on the base class by inheritance and adds a specic implementation of the base class's abstract `_algorithm()` method.

This way, when implementing a new indicator, the only thing the implementer has to worry about is how the particular indicator's algorithm works.

# Using an indicator:

```python
ma = MovingAverage(timeseries,period=25)
```

Have new data to add? The class automatically handles concatenation and calculating new output data. The datatype for an input is expected to be a list. The class implementation is naive, so it won't handle lots of different data-types, just a list.

```python
new_data = [5,7,12,14]

ma.update(new_data)
```

Access the raw data and algorithm output:

```python
raw_data = ma.rd()

output_data = ma.od()
```

You can also pass a `size=XXX` argument when instantiating a class. This will set the maximum size of the internal arrays (at this time typed as collections.deque). This is different from the algorithm period, ie the number of elements to run the algorithm over.

For example, if you only want to keep track of 100 days (and your period is <= 100) of data you would instantiate like this:

```python
indic = MovingAverage(size=100)
```

# Why use classes for these? Why not a bunch of functions?

This seems like a good application of OO principles and abstraction. These classes 'hide' the data structures for raw data and derived data from the user.

# Contributing

I welcome pull requests. Please implement unit tests that show your algorithm works (don't forget corner cases).

# TODO Implementation

[x] Moving Average
[ ] MACD (Moving Average Convergence Divergence)
[ ] RSI (Relative Strength Index)
[ ] OBV (On Balance Volume)
