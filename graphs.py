import pandas as pd
import plotly.express as px

df = pd.read_csv(r"C:\Users\bhuvi\Google Drive\WHJr\Python\Project 103 - dataVisualization\data.csv")

fig = px.scatter(df,    x="date",
                        y="cases",
                        color="country"
            )
fig.show()
