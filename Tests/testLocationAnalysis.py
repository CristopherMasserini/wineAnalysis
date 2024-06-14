import locationAnalysis

import pandas as pd
import unittest


def test_get_countries():
    data = locationAnalysis.get_countries('Files/winemag-data-small.csv')
    assert list(data.loc[:, 'counts'])[0] > 0
