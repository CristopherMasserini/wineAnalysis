import nltk
import pandas as pd
import string


def common_words_single_column(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """
    Determines most popular words in the description, broken down by the column given

    :param df: Pandas dataframe containing wine information and descriptions.
    :param col: Column to break down the description by. Examples: points, price, variety.

    :return: A Pandas dataframe of most common words and their frequencies for the column values.
    """

    descriptions = list(df.loc[:, 'description'])
    targetCol = list(df.loc[:, col])

    translator = str.maketrans('', '', string.punctuation)

    # Use this to group by target column and concat descriptions
    # df['text'] = df[['name', 'text', 'month']].groupby(['name', 'month'])['text'].transform(lambda x: ','.join(x))
    # df[['name', 'text', 'month']].drop_duplicates()

    for ind, value in enumerate(targetCol):
        desc = descriptions[ind].lower().translate(translator)  # Lowercase and remove punctuation
        descWords = nltk.word_tokenize(desc)
        non_stopwords = []
        for word in descWords:
            if word not in nltk.corpus.stopwords.words("english"):
                non_stopwords.append(word)
        fdist = nltk.probability.FreqDist(non_stopwords)



def common_words_multiple_column(df: pd.DataFrame, cols: list) -> dict:
    """
    Determines most popular words in the description, broken down by the columns given.

    :param df: Pandas dataframe containing wine information and descriptions.
    :param cols: Columns to break down the description by. Example: ['country', 'variety'].

    :return: A dictionary of most common words and their frequencies.
    """
    pass
