import plotly.graph_objs as go
import numpy as np
import pandas as pd
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
print(__version__)

init_notebook_mode(connected=True)

df = pd.read_csv('CSV Content/2014_World_GDP')
print(df.head())

data = dict(type='choropleth', locations=df['CODE'], z=df['GDP (BILLIONS)'],
            text=df['COUNTRY'], colorbar={'title': 'GDP in Billions USD'})

layout = dict(title='2014 Global GDP', geo=dict(
    showframe=False, projection={'type': 'mercator'}))

choromap = go.Figure(data=[data], layout=layout)

plot(choromap)
