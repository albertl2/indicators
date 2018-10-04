# -*- coding: utf-8 -*-
"""Financial technical analysis indicator base class.

This module contains the Indicator base class for inheritance for time-series
based financial indicators.
"""

from abc import abstractmethod
from collections import deque


class Indicator:
    """Base functionality for time-series based QA indicators.

    This is a naive implementation that does not check to see if your inputs
    are all the same types; i.e. a list of consistent type, or single variables
    of consistent type.
    """

    # TODO Make type agnostic (pandas DataFrame/Series, numpy arrays, others?)
    def __init__(self, *args, **kwargs):
        """Initialize with no arguments or some arguments.

        Args:
            args (:obj: `list` of :obj: `Number`): Time-series data.
            kwargs (:obj: `dict`): contains algorithm specific params.
                Inheriting classes will use these.

        Params:
            _rd: contains original time-series (_r_aw _d_ata)
            _od: contains same-as-rd indices (_o_utput _d_ata)
            size: sets max array length, indices < end-size fall off as new
                values are appended. Defaults to 100.

        """
        # Grab the size keyword value, or default to 100.
        self.size = kwargs.get('size',100)
        self._rd = deque(maxlen=self.size)
        self._od = deque(maxlen=self.size)

        # Unpack the tuple so that the update method can be used internally and
        # externally.
        self.update(*args)


    def update(self, *args):
        """Adds new raw data to rd, then (re)runs the algorithm and updates od.

        Append args to the end of rd and apply the indicator's algorithm to
        only the list entries affected.
        """
        try:
            for arg in args:
                self._rd += arg
        except TypeError:
            self._rd += args
        self._algorithm()

    @abstractmethod
    def _algorithm(self):
        '''
        When implementing an indicator, you must override this method.
        '''
        self._od = self._rd

    def rd(self):
        '''
        Getter for raw data contained in the _rd deque. Returns a list.
        '''
        return list(self._rd)

    def od(self):
        '''
        Getter for output data contained in the _od deque. Returns a list.
        '''
        return list(self._od)
