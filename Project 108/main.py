import csv 
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff

df = pd.read_csv("Student Marks vs Days Present.csv")
fig = ff.create_distplot([df['Marks'].tolist()],['Marks'], show_hist= False)
fig.show()