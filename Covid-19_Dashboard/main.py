#!/usr/bin/python

import pandas as pd
import numpy as np
from jinja2 import Template
import sys

URL_Confirmed = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data' \
                '/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv '
URL_Deaths = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data' \
             '/csse_covid_19_time_series/time_series_covid19_deaths_global.csv '
URL_Recovered = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data' \
                '/csse_covid_19_time_series/time_series_covid19_recovered_global.csv '

# -->Confirmed
dfConfirmed = pd.read_csv(URL_Confirmed)
dfConfirmed = dfConfirmed.replace(np.nan, '', regex=True)

try:
    _Country = sys.argv[1]
except:
    sys.exit(1)
try:
    _State = sys.argv[2]
except:
    _State = ''

_Confirmed = dfConfirmed.loc[(dfConfirmed['Country/Region'] == _Country) & (dfConfirmed['Province/State'] == _State)]

Confirmed = _Confirmed.to_numpy()

_index = dfConfirmed.columns[1:].to_numpy()

# -->Deaths

dfDeaths = pd.read_csv(URL_Deaths)
dfDeaths = dfDeaths.replace(np.nan, '', regex=True)

_Deaths = dfDeaths.loc[(dfDeaths['Country/Region'] == _Country) & (dfDeaths['Province/State'] == _State)]

Deaths = _Deaths.to_numpy()

# -->Recovered
dfRecovered = pd.read_csv(URL_Recovered)
dfRecovered = dfRecovered.replace(np.nan, '', regex=True)

_Recovered = dfRecovered.loc[(dfRecovered['Country/Region'] == _Country) & (dfRecovered['Province/State'] == _State)]

Recovered = _Recovered.to_numpy()

template = Template(open('Covid-19_SVG_Template.svg').read())
out = template.render(Country=_Country, State=_State, index=str(_index[-1]), data_c=f"{int(Confirmed[0][-1]):,d}",
                      data_r=f"{int(Recovered[0][-1]):,d}",
                      data_d=f"{int(Deaths[0][-1]):,d}")

with open("Covid-19.svg", "w") as outfile:
    outfile.write(out)
