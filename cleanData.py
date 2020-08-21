"""
Xinyue Ma(Mary), Ziqi Chen(Vicky)
CSE163-Final-Project: Happiness Factors
CSE 163 AC

This file implements function to clean and analyze data from
GDP in 2019, geospatial data in the world and Happiness Score data in 2019
"""

import numpy as np


# Part1 Clean Data
# refine data according to the prompt (set United States as United States of
# America)
def clean_map_data(data_2019, geo_df):
    """
    Takes data_2019, geo_df as parameters
    Filters the data that we need to construct the Choropleth Map
    Returns the filtered data(geo_merge)
    """
    column = data_2019.columns
    row = data_2019[data_2019['Country or region'] == 'United States'].index[0]
    usa = 'United States of America'
    data_2019.iloc[row, column.get_loc('Country or region')] = usa
    country_score = data_2019[['Country or region', 'Score']]
    country_geometry = geo_df[['SOVEREIGNT', 'geometry']]
    geo_merge = country_geometry.merge(country_score, left_on='SOVEREIGNT',
                                       right_on='Country or region',
                                       how='left')
    return geo_merge


# Part2 Clean Data
def clean_gdp_data(data_2019, gdp_file):
    """
    Takes data_2019, gdp_file as parameters
    Filters columns we need and then merge data by Country name
    Returns gdp_merged
    """
    top20_happiness = data_2019[['Country or region', 'Score']].head(20)
    gdp_2019 = gdp_file[['Country Name', '2019']]
    gdp_merged = top20_happiness.merge(gdp_2019, left_on='Country or region',
                                       right_on='Country Name', how='left')
    return gdp_merged


# Part3 Clean Data
def clean_correlation_data(data_2019):
    """
    Takes data_2019 as a parameter
    Calculates the correlation for each Happiness indicators
    Returns the correlaion as numpy
    """
    extract = data_2019[['Score', 'GDP per capita',
                         'Social support', 'Healthy life expectancy',
                         'Freedom to make life choices', 'Generosity',
                         'Perceptions of corruption']]
    col = extract.columns
    for name in col:
        extract = extract[extract[name].notnull()]
    score = extract[['Score']]
    score_li = np.array(score)
    construct = score_li.reshape(1, len(score))

    for column in col:
        if column != "Score":
            element = extract[[column]]
            column = np.array(element)
            reshape = column.reshape(1, len(element))
            construct = np.append(construct, reshape, axis=0)
    correlation = np.corrcoef(construct)
    return correlation
