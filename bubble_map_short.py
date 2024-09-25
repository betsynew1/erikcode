# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 18:57:12 2024

@author: eeinset
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import plotly.io as pio
pio.renderers.default = 'browser'

#---------------------------------------------------------------
# READ THE DATA FILE AND LOAD THE DATAFRAME WITH LAT AND LON
# Make sure there are no commas in the number columns and it is
#   ok to have spaces between the text strings of city names

de = pd.read_csv('../../ETSchools.csv')
dc = pd.read_csv('../../US_colleges2.txt',dtype={'ZIP':str})

#---------------------------------------------------------------
# PLOT THE MAP

fig = ''

# ET School map
fig = px.scatter_geo(de, lat="lat", lon="lon",
                     scope='world', projection="orthographic",
                     hover_data=['School_Name','State'])

# US College overlay
fig.add_trace(go.Scattergeo(lat=dc['lat'],lon=dc['lon'],name='Colleges',
                            text=dc['NAME']))

fig.update_layout(title="Map", showlegend=True)

fig.show()

#---------------------------------------------------------------