# -*- coding: utf-8 -*-
"""Implementation of simple moving average.

This module contains an implementation of a simple moving average accord()ing to

https://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:moving_averages

"""

import numbers
from indicator import *


class MovingAverage(Indicator):
    """Class for calculating a simple moving average on the fly.

    All of the data handling is done by the Indicator class. Our only concern
    here are the time_series, kwargs (which house the algorithm params) and the
    algorithm for determining the indicator's output.
    """

    def __init__(self, *time_series, **kwargs):
        """Class initialization, allows for some or no args.

        Args:
            time_series (:obj:`list` of :obj:`Number`): a time-series of
            numerical values
            kwargs (:obj:'dict'): contains algorithm specific
            parameters.

        """
        # Instantiate some parameters for a moving average.
        self.period = 1

        # Apply kwargs, if there are any.
        if len(kwargs) > 0:
            self.period = kwargs.get('period')

        # Init Indicator class (includes running _algorithm).
        super().__init__(*time_series)

    def _algorithm(self):
        for i in range(len(self.rd())):
            if i >= self.period - 1:
                start = i-self.period+1
                end = i+1
                # Filter out strings in summation window.
                to_sum = [
                        i for i in self.rd()[start:end]
                        if isinstance(i, numbers.Number)
                        ]

                # The length of to_sum will generally reflect the period of the
                # moving average, except when a non-number is present. Then the
                # lenth of to_sum will reflect the number to divide by in order
                # to get an average of availble values.
                avg = sum(to_sum)/len(to_sum)
            else:
                self._od.append('')
