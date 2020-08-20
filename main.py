
import pandas as pd
import geopandas as gpd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np

import cleanData


def plot_task1(data_2019, geo_df):

    geo_merge = cleanData.clean_task1(data_2019, geo_df)
    geo_filtered = geo_merge[geo_merge['Score'].notnull()]

    fig, ax = plt.subplots(1)
    geo_merge.plot(color= '#CCCCCC', ax=ax)
    geo_filtered.plot(column='Score', cmap='OrRd', ax=ax, legend=True)

    plt.title('Happiness Score Map')
    plt.savefig('Happiness Score map.png')
    plt.show()



def plot_task2(data_2019, gdp):
    gdp_merged = cleanData.clean_task2(data_2019, gdp)
    fig = px.scatter(gdp_merged, x='Country Name', y='2019', color='Score',
                 size='Score', log_y=True,
                 labels={
                    'Country Name': 'Countries',
                    '2019': 'GDP in 2019'})
    fig.update_layout(title={
                    'text': "Top20 Happiest Countries With Their GDP",
                    'y':0.96,
                    'x':0.5,
                    'xanchor': 'center',
                    'yanchor': 'top'})

    fig.show()


def analyze_task3(data_2019):
    nump = cleanData.clean_task3(data_2019)
    print(nump)



def main():
    geo_df = gpd.read_file('data/geo-data/ne_110m_admin_0_countries.shp')
    data_2019 = pd.read_csv('data/datasets-894-813759-2019.csv')
    gdp = pd.read_csv('data/gdp.csv')

    #plot_task1(data_2019, geo_df)
    #plot_task2(data_2019, gdp)
    analyze_task3(data_2019)


if  __name__ == '__main__':
    main()