import locationAnalysis

import pandas as pd
import unittest


def test_get_countries():
    data = locationAnalysis.get_countries('Files/winemag-data-small.csv',
                                          'Files/winemag-data-small_grouped.csv')
    assert list(data.loc[:, 'counts'])[0] > 0


def test_plot_countries():
    plotted = locationAnalysis.plot_countries('Files/winemag-data-small_grouped.csv')
    assert plotted is True
