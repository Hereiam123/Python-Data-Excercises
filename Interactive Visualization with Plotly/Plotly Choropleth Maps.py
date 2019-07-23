import plotly.graph_objs as go
import numpy as np
import pandas as pd
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
print(__version__)

init_notebook_mode(connected=True)

data = dict(type='choropleth', locations=[
            'AZ', 'CA', 'NY'], locationmode='USA-states', colorscale='Portland', text=['text 1', 'text 2', 'text 3'], z=[1.0, 2.0, 3.0], colorbar={'title': 'Colorbar Title'})

print(data)

layout = dict(geo={'scope': 'usa'})

#Use go figure to output map
choromap = go.Figure(data=[data], layout=layout)
plot(choromap)
