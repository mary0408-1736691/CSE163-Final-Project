import pandas as pd
import geopandas as gpd
import plotly.express as px
import matplotlib.pyplot as plt
from plotly.subplots import make_subplots
import plotly.graph_objects as go
#geo_df = gpd.read_file('data/geo-data/ne_110m_admin_0_countries.shp')

data_2019 = pd.read_csv('data/happiness-score.csv')
gdp = pd.read_csv('data/gdp.csv')



 # Part1 Clean Data

#country_score = data_2019[['Country or region', 'Score']]
#country_geometry = geo_df[['SOVEREIGNT', 'geometry']]
#geo_merge = country_geometry.merge(country_score, left_on='SOVEREIGNT', right_on='Country or region', how='left')


# Part2 Clean Data
top20_happiness = data_2019[['Country or region', 'Score']].head(20)
gdp_2019 = gdp[['Country Name', '2019']]
gdp_merged = top20_happiness.merge(gdp_2019, left_on='Country or region',
                                   right_on='Country Name', how='left')

# Plot gdp-happiness
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