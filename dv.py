import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")
fig = px.line(df, x="Date", y="Per capita income", color="Country", title='Per Capita Income')
fig.show()