import cleaning
import geopandas
import folium

def get_countries(filePath):
    """
    Gets the countries out of the data set and the counts at each

    :return: pandas df of countries and counts
    """
    data = cleaning.load_file(filePath, False)
    data = cleaning.clean_columns(data)

    data = data.groupby(['country']).size().reset_index(name='counts')
    return data


