import plotly
from plotly.graph_objs import Layout, Heatmap
#plotly.tools.set_credentials_file(username='ricorx7', api_key='0tRCw1J7ViBrCRfhDZ8y')


plotly.offline.plot({
    "data": [Heatmap(z=[[1, 20, 30],
           [20, 1, 60],
           [30, 60, 1]])],
    "layout": Layout(title="A Heatmap")
})

