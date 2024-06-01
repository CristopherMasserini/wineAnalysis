import nltk
import pandas as pd
import string


def common_words_single_column(df: pd.DataFrame, col: str) -> dict:
    """
    Determines most popular words in the description, broken down by the column given

    :param df: Pandas dataframe containing wine information and descriptions.
    :param col: Column to break down the description by. Examples: points, price, variety.

    :return: A Pandas dataframe of most common words and their frequencies for the column values.
    """

    translator = str.maketrans('', '', string.punctuation)
    stopwords = nltk.corpus.stopwords.words("english")

    # Use this to group by target column and concat descriptions
    dfNew = df[[col]]
    dfNew['all_descriptions'] = df[[col, 'description']].groupby([col])['description'].transform(lambda x: ' '.join(x))
    dfNew = dfNew.drop_duplicates()

    descriptions = list(dfNew.loc[:, 'all_descriptions'])
    targetCol = list(dfNew.loc[:, col])

    info = {}

    for ind, value in enumerate(targetCol):
        desc = descriptions[ind].lower().translate(translator)  # Lowercase and remove punctuation
        descWords = nltk.word_tokenize(desc)
        non_stopwords = []
        for word in descWords:
            if word not in stopwords:
                non_stopwords.append(word)
        fdist = nltk.probability.FreqDist(non_stopwords)

        info[value] = fdist.most_common(20)

    return info



def common_words_multiple_column(df: pd.DataFrame, cols: list) -> dict:
    """
    Determines most popular words in the description, broken down by the columns given.

    :param df: Pandas dataframe containing wine information and descriptions.
    :param cols: Columns to break down the description by. Example: ['country', 'variety'].

    :return: A dictionary of most common words and their frequencies.
    """
    pass
