import pandas as pd
import string


def common_words_single_column(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """
    Determines most popular words in the description, broken down by the column given

    :param df: Pandas dataframe containing wine information and descriptions.
    :param col: Column to break down the description by. Examples: points, price, variety.

    :return: A Pandas dataframe of most common words and their frequencies for the column values.
    """
    colValues = []
    words = []
    counts = []

    descriptions = list(df.loc[:, 'description'])
    targetCol = list(df.loc[:, col])

    translator = str.maketrans('', '', string.punctuation)

    for ind, value in enumerate(targetCol):
        desc = descriptions[ind].lower().translate(translator)  # Lowercase and remove punctuation
        descWords = desc.split(' ')
        for word in descWords:
            if word in words:
                wordInd = words.index(word)
                counts[wordInd] += 1
            else:
                colValues.append(value)
                counts.append(1)
                words.append(word)

    # return wordDict


def common_words_multiple_column(df: pd.DataFrame, cols: list) -> dict:
    """
    Determines most popular words in the description, broken down by the columns given.

    :param df: Pandas dataframe containing wine information and descriptions.
    :param cols: Columns to break down the description by. Example: ['country', 'variety'].

    :return: A dictionary of most common words and their frequencies.
    """
    pass
