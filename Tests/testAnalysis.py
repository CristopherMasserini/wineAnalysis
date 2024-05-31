import analysis

import pandas as pd
import unittest

data = pd.read_csv('Files/winemag-data-small.csv')


def test_common_words_single_column():
    analysis.common_words_single_column(data, 'variety')
