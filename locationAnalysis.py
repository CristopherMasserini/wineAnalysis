import cleaning
import geopandas
import folium

def get_countries():
    """
    Gets the countries out of the data set and the counts at each

    :return: pandas df of countries and counts
    """
    data = cleaning.load_file('Files/winemag-data-130k-v2.csv')
    data = cleaning.clean_columns(data)


