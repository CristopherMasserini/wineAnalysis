import locationAnalysis

import pandas as pd
import unittest


def test_get_countries_counts():
    data = locationAnalysis.get_countries('Files/winemag-data-small.csv',
                                          'Files/winemag-data-small_grouped.csv')
    assert list(data.loc[:, 'counts'])[0] > 0

def test_get_countries_averages():
    data = locationAnalysis.get_countries('Files/winemag-data-small.csv',
                                          'Files/winemag-data-small_grouped.csv',
                                          False)
    assert list(data.loc[:, 'averagePoints'])[0] > 80
    assert list(data.loc[:, 'averagePoints'])[0] < 100


def test_plot_countries():
    plotted = locationAnalysis.plot_countries('Files/winemag-data-small_grouped.csv')
    assert plotted is True

def test_country_translation():
    df = locationAnalysis.get_countries('Files/winemag-data-small.csv',
                                        'Files/winemag-data-small_grouped.csv')

    dfNew = locationAnalysis.country_translation(df)
    countries = list(dfNew.loc[:, 'country'])

    assert 'US' not in countries
    assert 'United States of America' in countries
