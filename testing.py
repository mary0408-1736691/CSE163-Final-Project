"""
Xinyue Ma(Mary), Ziqi Chen(Vicky)
CSE163-Final-Project: Happiness Factors
CSE 163 AC

This file tests whether we prepared the data correctly for plotting figures
"""
from cse163_utils import assert_equals
import cleanData
import pandas as pd
import geopandas as gpd


def test_clean_map_data(data_2019, geo_df):
    """
    Takes data_2019 and geo_df as parameters
    Checks the number of columns in the cleaned data
    """
    assert_equals(4, len(cleanData.clean_map_data(data_2019, geo_df).columns))


def test_clean_gdp_data(data_2019, gdp_file):
    """
    Takes data_2019 and gdp_file as parameters
    Checks the number of rows in the cleaned data and
    the number of columns in the cleaned data
    """
    assert_equals(20, len(cleanData.clean_gdp_data(data_2019, gdp_file)))
    assert_equals(4,
                  len(cleanData.clean_gdp_data(data_2019, gdp_file).columns))


def test_clean_correlation_data(data_2019):
    """
    Takes data_2019 as a parameter
    Check the shape of numpy array to match the number of elements in axis
    we want in later plot
    """
    assert_equals((7, 7), cleanData.clean_correlation_data(data_2019).shape)


def main():
    geo_df = gpd.read_file('data/geo-data/ne_110m_admin_0_countries.shp')
    data_2019 = pd.read_csv('data/datasets-894-813759-2019.csv')
    gdp = pd.read_csv('data/gdp.csv')
    test_clean_map_data(data_2019, geo_df)
    test_clean_gdp_data(data_2019, gdp)
    test_clean_correlation_data(data_2019)


if __name__ == '__main__':
    main()
