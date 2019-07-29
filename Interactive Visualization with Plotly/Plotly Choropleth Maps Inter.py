import plotly.graph_objs as go
import numpy as np
import pandas as pd
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
print(__version__)

init_notebook_mode(connected=True)

# Z is data represented
data = dict(type='choropleth', locations=[
            'AZ', 'CA', 'NY'], locationmode='USA-states', colorscale='Portland', text=['Arizona', 'California', 'New York'], z=[1.0, 2.0, 3.0], colorbar={'title': 'Colorbar Title'})

print(data)

# Define as a US states layout
layout = dict(geo={'scope': 'usa'})

# Use go figure to output map
choromap = go.Figure(data=[data], layout=layout)
plot(choromap)

df = pd.read_csv('CSV Content/2011_US_AGRI_Exports')
print(df.head())

# Markers
data = dict(type='choropleth', colorscale='YlOrRd',
            locations=df['code'], locationmode='USA-states', z=df['total exports'], text=df['text'], marker=dict(line=dict(color='rgb(255,255,255)', width=2)), colorbar={'title': 'Millions USD'})

layout = dict(title='2011 US Agriculture Exports by State', geo=dict(
    scope='usa', showlakes=True, lakecolor='rgb(85,173,240)'))

choromap2 = go.Figure(data=[data], layout=layout)

plot(choromap2)
