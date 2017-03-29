import plotly
from plotly.graph_objs import Layout, Heatmap

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/volcano.csv')

data = [Heatmap( z=df.values.tolist(), colorscale='Viridis')]

plotly.offline.plot({
    "data": data,
    "layout": Layout(title="hello world")
})