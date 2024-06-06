import analysis

import pandas as pd
import unittest

data = pd.read_csv('Files/winemag-data-small.csv')

def test_common_words_single_column():
    infoDict = analysis.common_words_single_column(data, 'variety')
    assert isinstance(infoDict['Merlot'], list)
    assert len(infoDict['Merlot']) > 0


def test_single_column_reduce():
    infoDict = analysis.single_column_reduce(data, 'variety')
    assert isinstance(infoDict['Merlot'], list)
    assert len(infoDict['Merlot']) > 0


def test_vectorize_descriptions():
    vector = analysis.vectorize_descriptions(data)
    assert vector.shape[0] > 0
    assert vector.shape[1] > 0


def test_all():
    test_common_words_single_column()
    test_single_column_reduce()
    test_vectorize_descriptions()
