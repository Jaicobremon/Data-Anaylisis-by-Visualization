#Importing all modules
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import csv

#Reading csv file
df = pd.read_csv("StudentLevels.csv")

#Calculating mean of attempts per level
print(df.groupby("level")["attempt"].mean())

#Creating variable to store mean
mean = df.groupby(["student_id","level"],as_index = False)["attempt"].mean()

#Creating graph
graph = px.scatter(mean,  x = "student_id", y = "level", color = "attempt", size = "attempt")

#Showing graph
graph.show()