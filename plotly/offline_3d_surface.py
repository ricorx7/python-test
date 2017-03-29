import plotly
from plotly.graph_objs import Layout, Surface

import pandas as pd

# Read data from a csv
z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')

data = [
    Surface(
        z=z_data.as_matrix()
    )
]
layout = Layout(
    title='Mt Bruno Elevation',
    autosize=False,
    width=500,
    height=500,
    margin=dict(
        l=65,
        r=50,
        b=65,
        t=90
    )
)

plotly.offline.plot({
    "data": data,
    "layout": layout
})
