## CSE163-Final-Project: “Happiness Factors”
#### Authors: Xinyue Ma(Mary), Ziqi Chen(Vicky)

#### 1. Libaries needed before running the program
  * pandas: use this library as a tool to manipulate dataframes.
  * geopandas: use this library to analyze geospatial data.
  * plotly: use this library to draw scatter-plot and Heatmap.
  * matplotlib: use this library to draw the Choropleth Map.
  * numpy: use this library to calculate correlation

#### 2. Data
  * We already submitted the data. All data saved in the file called data.
  * We elinimate the blank lines in 'gdp.csv' for making the process of reading data successful

#### 3. Files Construction  
  * The whole program code are splited into three files(cleanData.py, main.py, testing.py)
  * cleanData.py: this file cleans the data needed for main.py
  * mian.py: this file does the major job on analyzing and ploting
  * testing.py: this file tests whether we prepared data correctly in cleanData.py

#### 4. Running Instruction 
  * Download the repository as a folder that inlcudes all files. 
  * Please set directory to the location of the project folder to maintain the programs works, since we set relative path to read data in main.py.
  * You can run code through main.py 
  * If you want to see the first map figure in plot_world_happy, please make  two plot funtions commented (#plot_gdp_happy(data_2019, gdp)) and (#plot_correlation(data_2019)) in main function in main.py. 
Same ways if you want to see the other figures. 


  * You will get a figure called 'Happiness Score map.png' that presents the Happiness Score Distribution in the word in 2019 when runing a function called plot_world_happy.
  * You will see a scatter plot that descibes the relationship between Economy and happiness score among the top 10 countries that have high happiness scores when running the function called plot_gdp_happy.
  * You will get a HeatMap that demonstrates the correlation bettween each Happiness indicators.


 #### 5. Other things 
  * Import the cleanData.py in main.py, since we need the data cleaned by the functions in cleanData.py
