import cleaning

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt


def get_countries(filePath: str, saveFilePath: str, counts=True):
    """
    Gets the countries out of the data set and the counts at each

    :return: pandas df of countries and counts
    """
    data = cleaning.load_file(filePath, False)
    data = cleaning.clean_columns(data)

    if counts:
        data = data.groupby(['country']).size().reset_index(name='counts')
    else:
        data = data.groupby(['country'])['points'].mean().reset_index(name='averagePoints')
    data.to_csv(saveFilePath, index=False)
    return data


def country_translation(df: pd.DataFrame):
    """
    Gets one name of a country and translates it into other format
    Ex. US -> United States of America
    :param df: dataframe of the countries
    :return: dataframe with names translated
    """

    countryNames = list(df.loc[:, 'country'])

    names = {
        'US': 'United States of America',
        'Bosnia and Herzegovina': 'Bosnia and Herz.',
        'England': 'United Kingdom',
        'Czech Republic': 'Czechia',
        'Macedonia': 'North Macedonia'
    }

    for key, value in names.items():
        try:
            countryInd = countryNames.index(key)
            df.at[countryInd, 'country'] = value
        except ValueError:
            # Country not in data
            pass

    return df


def plot_countries(filePath):
    """
    Plots

    :param filePath: file path of grouped countries
    """
    countries = pd.read_csv(filePath)
    countries = country_translation(countries)

    gdf = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

    try:
        gdf = gdf.merge(countries, how='outer', left_on='name', right_on='country')

        fig = gdf.plot(column='counts', cmap='Purples', legend=True,
                       missing_kwds={"color": "black", "edgecolor": "red",
                                     "hatch": "///", "label": "No Reviews"}
                       )
        fig.axis('off')
        plt.show()
        return True
    except Exception:
        return False


if __name__ == '__main__':
    get_countries('Files/winemag-data-130k-v2.csv',
                  'Files/winemag-data-130k-v2_grouped.csv')
    plot_countries('Files/winemag-data-130k-v2_grouped.csv')
