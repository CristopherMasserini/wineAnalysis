import cleaning

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt


def get_countries(filePath: str, saveFilePath: str):
    """
    Gets the countries out of the data set and the counts at each

    :return: pandas df of countries and counts
    """
    data = cleaning.load_file(filePath, False)
    data = cleaning.clean_columns(data)

    data = data.groupby(['country']).size().reset_index(name='counts')
    data.to_csv(saveFilePath, index=False)
    return data


def plot_countries(filePath):
    """
    Plots

    :param filePath: file path of grouped countries
    """
    countries = pd.read_csv(filePath)
    gdf = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

    try:
        gdf = gdf.merge(countries, how='outer', left_on='name', right_on='country')
        # gdf['counts'] = gdf['counts'].fillna(0)

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
