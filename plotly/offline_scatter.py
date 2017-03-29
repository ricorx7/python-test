import plotly
import plotly.plotly as py
from plotly.graph_objs import Scatter, Layout, Heatmap
plotly.tools.set_credentials_file(username='ricorx7', api_key='0tRCw1J7ViBrCRfhDZ8y')

import pandas as pd

plotly.offline.plot({
    "data": [Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])],
    "layout": Layout(title="hello world")
})


df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/volcano.csv')

data = [Heatmap( z=df.values.tolist(), colorscale='Viridis')]

py.iplot(data, filename='pandas-heatmap')


