import nltk
import pandas as pd
import string
from sklearn.feature_extraction.text import CountVectorizer


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


def single_column_reduce(df: pd.DataFrame, col: str) -> dict:
    """
    Creates a dictionary of each value of the column and a list of the descriptions.

    :param df: Pandas dataframe containing wine information and descriptions.
    :param col: Column to break down the description by. Examples: points, price, variety.

    :return: A dictionary of each description (in a list) for each value of col
    """
    descriptions = list(df.loc[:, 'description'])
    targetCol = list(df.loc[:, col])

    data = {}

    for ind, value in enumerate(targetCol):
        desc = descriptions[ind]
        if value in data:
            data[value].append(desc)
        else:
            data[value] = [desc]

    return data


def vectorize_descriptions(df: pd.DataFrame) -> object:
    """
    Vectorizing the descriptions to be used in a bag of words model approach.
    :param df: Pandas dataframe containing wine descriptions.
    :return: Vecotrized  list of the vocabulary.
    """

    vectorizer = CountVectorizer()
    translator = str.maketrans('', '', string.punctuation)

    descriptions = list(df.loc[:, 'description'])
    cleaned_descriptions = []

    for description in descriptions:
        desc = description.lower().translate(translator)
        cleaned_descriptions.append(desc)

    vectorizer.fit(cleaned_descriptions)
    vector = vectorizer.transform(cleaned_descriptions)
    return vector

