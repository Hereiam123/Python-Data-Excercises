import pandas as pd
import numpy as np
import cufflinks as cf
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

# Connect interactivity with JS library
init_notebook_mode(connected=True)

# Create offline option
cf.go_offline()


df = pd.DataFrame(np.random.randn(100, 4), columns='A B C D'.split())
print(df.head())

df2 = pd.DataFrame({'Category': ['A', 'B', 'C'], 'Values': [32, 43, 50]})
print(df2.head())

df.iplot(kind='scatter', x='A', y='B')
