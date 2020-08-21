"""
Xinyue Ma(Mary), Ziqi Chen(Vicky)
CSE163-Final-Project: Happiness Factors
CSE 163 AC

This file imports functions from cleanData.py. Besides, this file
also plots figures for analzing data from
GDP in 2019, geospatial data in the world and Happiness Score data in 2019
"""


import pandas as pd
import geopandas as gpd
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go
# import functions from cleanData.py
import cleanData


def plot_world_happy(data_2019, geo_df):
    """
    Takes data_2019 and geo_df as parameters
    Plots a Choropleth Map that contains Happiness Scores distribution
    Saves the figure as "Happiness Score map.png" and shows the figure

    """
    geo_merge = cleanData.clean_map_data(data_2019, geo_df)
    geo_filtered = geo_merge[geo_merge['Score'].notnull()]

    fig, ax = plt.subplots(1)
    geo_merge.plot(color='#CCCCCC', ax=ax)
    geo_filtered.plot(column='Score', cmap='OrRd', ax=ax, legend=True)

    plt.title('Happiness Score Map')
    plt.savefig('Happiness Score map.png')
    plt.show()


def plot_gdp_happy(data_2019, gdp):
    """
    Takes data_2019 and gdp as parameters
    Plots a scatter plot to show the relationship between
    Economy and Happiness Score for top 10 country
    Shows the plot
    """
    gdp_merged = cleanData.clean_gdp_data(data_2019, gdp)
    fig = px.scatter(gdp_merged, x='Country Name', y='2019', color='Score',
                     size='Score', log_y=True,
                     labels={
                        'Country Name': 'Countries',
                        '2019': 'GDP in 2019'})
    fig.update_layout(title={
                    'text': "Top20 Happiest Countries With Their GDP",
                    'y': 0.96,
                    'x': 0.5,
                    'xanchor': 'center',
                    'yanchor': 'top'})

    fig.show()


def plot_correlation(data_2019):
    """
    Takes data_2019 as a parameter
    Plots a heatmap that demonstrates the correlation between
    Happiness indicators and shows the figure
    """
    nump = cleanData.clean_correlation_data(data_2019)
    axis_label = ['Score', 'GDP per capita', 'Social support',
                  'Healthy life expectancy', 'Freedom to make life choices',
                  'Generosity', 'Perceptions of corruption']
    corr_map = go.Figure(data=go.Heatmap(
        z=nump,
        x=axis_label,
        y=axis_label,
        colorscale='Viridis'))
    corr_map.update_layout(
        title={
            'text': "Correlations Between Factors of Happiness",
            'y': 0.96,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        xaxis_nticks=30,
        yaxis_nticks=30)
    corr_map.show()


def main():
    geo_df = gpd.read_file('data/geo-data/ne_110m_admin_0_countries.shp')
    data_2019 = pd.read_csv('data/datasets-894-813759-2019.csv')
    gdp = pd.read_csv('data/gdp.csv')

    plot_world_happy(data_2019, geo_df)
    plot_gdp_happy(data_2019, gdp)
    plot_correlation(data_2019)


if __name__ == '__main__':
    main()
