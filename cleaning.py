import pandas as pd


def load_file(fileName: str, printInfo=False) -> pd.DataFrame:
    """
    Loads the file and prints basic information

    :param fileName: file name of data
    :param printInfo: to print the data or not
    :return: pandas dataframe of the data
    """

    df = pd.read_csv(fileName)

    if printInfo:
        print(df.head())
        print(df.columns)
        print(df.info())

    return df


def clean_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Drops unnecessary column and removes any null values (in specific columns)

    :param df: pandas dataframe of the data

    :return: cleaned pandas dataframe
    """
    df = df.drop('Unnamed: 0', axis=1)
    df.dropna(subset=['description', 'variety', 'country', 'points'], inplace=True)
    return df


if __name__ == '__main__':
    data = load_file('Files/winemag-data-130k-v2.csv', True)
    data = clean_columns(data)
