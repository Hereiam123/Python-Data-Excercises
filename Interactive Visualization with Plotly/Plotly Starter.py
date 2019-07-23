import plotly.graph_objs as go
import numpy as np
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
print(__version__)  # requires version >= 1.9.0

# Always run this the command before at the start of notebook
init_notebook_mode(connected=True)

x = np.array([2, 5, 8, 0, 2, -8, 4, 3, 1])
y = np.array([2, 5, 8, 0, 2, -8, 4, 3, 1])


data = [go.Scatter(x=x, y=y)]
fig = go.Figure(data=data, layout=go.Layout(title='Offline Plotly Testing', width=800, height=500,
                                            xaxis=dict(title='X-axis'), yaxis=dict(title='Y-axis')))


plot(fig, show_link=False)
