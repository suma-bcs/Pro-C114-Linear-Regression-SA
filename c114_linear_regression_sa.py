# -*- coding: utf-8 -*-
"""C114 linear regression SA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NYRwEYc_Wr69yoUSiuORgb4JZ5ewP-J1
"""

#Uploading the csv
from google.colab import files
data_to_load = files.upload()

"""We have uploaded the data for students admission. Now let's plot the GRE Score as X-Coordinate and the Chance of Admit as Y-Coordinate on the plot."""

import pandas as pd
import plotly.express as px

df = pd.read_csv("main.csv")

GRE_Score = df["GRE Score"].tolist()
Chances_of_admit = df["Chance of Admit "].tolist()

fig = px.scatter(x=GRE_Score, y=Chances_of_admit)
fig.show()

m = 0.01
c = -2.5
y = []
for x in GRE_Score:
  y_value = m*x + c
  y.append(y_value)

#Plotting the points
fig = px.scatter(x=GRE_Score, y=Chances_of_admit)
fig.update_layout(shapes=[
    dict(
      type= 'line',
      y0= min(y), y1= max(y),
      x0= min(GRE_Score), x1= max(GRE_Score)
    )
])
fig.show()

"""Here, the M is the slope of the line and the C is the intercept of the line.
let's see if we can predict the chance of admit of a person in a university based on the GRE Score.
"""

x = 600
y = m * x + c
print(f"Chances of admit of someone based on their GRE Score {x} is {y}")

"""We found the values of slope and intercept through the hit and trial methods .
Now let's check the computer algorithm for finding the slope and intercept.
"""

import numpy as np
GRE_Score_array = np.array(GRE_Score)
Chance_of_admit_array = np.array(Chances_of_admit)

#Slope and intercept using pre-built function of Numpy
m, c = np.polyfit(GRE_Score_array,Chance_of_admit_array,1)

y = []
for x in GRE_Score_array:
  y_value = m*x + c
  y.append(y_value)

#plotting the graph
fig = px.scatter(x=GRE_Score_array, y=Chance_of_admit_array)
fig.update_layout(shapes=[
    dict(
      type= 'line',
      y0= min(y), y1= max(y),
      x0= min(GRE_Score_array), x1= max(GRE_Score_array)
    )
])
fig.show()

x = 600
y = m * x + c
print(f"Chances of admit of someone based on their GRE Score {x} is {y}")

"""The chance of admit value we got by using our algorithm was 3.5 and the value we get by computer algorithm is 3.5 which is same.
We just created a prediction algorithm here.

"""