import pandas as pd


def common_words_single_column(df: pd.DataFrame, col: str) -> dict:
    """
    Determines most popular words in the description, broken down by the column given

    :param df: Pandas dataframe containing wine information and descriptions.
    :param col: Column to break down the description by. Examples: points, price, variety.

    :return: A dictionary of most common words and their frequencies.
    """
    pass


def common_words_multiple_column(df: pd.DataFrame, cols: list) -> dict:
    """
    Determines most popular words in the description, broken down by the columns given.

    :param df: Pandas dataframe containing wine information and descriptions.
    :param cols: Columns to break down the description by. Example: ['country', 'variety'].

    :return: A dictionary of most common words and their frequencies.
    """
    pass
