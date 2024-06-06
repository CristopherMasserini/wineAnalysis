import cleaning

import pandas as pd
import unittest

data = pd.read_csv('Files/winemag-data-small.csv')


def test_load_file():
    df = cleaning.load_file('Files/winemag-data-small.csv')
    assert isinstance(df, pd.DataFrame)
    assert len(list(df.description)) == 100
    assert list(df.loc[:, 'variety'])[10] is not None


def test_clean_columns():
    dfNew = cleaning.clean_columns(data)
    assert isinstance(dfNew, pd.DataFrame)
    assert len(list(dfNew.description)) > 0
    assert list(dfNew.loc[:, 'variety'])[10] is not None


def test_all():
    test_load_file()
    test_clean_columns()
