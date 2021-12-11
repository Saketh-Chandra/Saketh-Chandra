#!/usr/bin/python

from datetime import datetime
import pandas as pd
import numpy as np
from jinja2 import Template
import sys
from requests import get

URL_Confirmed = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data' \
                '/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv '
URL_Deaths = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data' \
             '/csse_covid_19_time_series/time_series_covid19_deaths_global.csv '
URL_Recovered = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data' \
                '/csse_covid_19_time_series/time_series_covid19_recovered_global.csv '

URL_Clock_UTC = 'https://www.worldtimeapi.org/api/timezone/Etc/UTC.json'

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

UTC_time = get(URL_Clock_UTC).json()["utc_datetime"]
dateTime = datetime.strptime(UTC_time, '%Y-%m-%dT%H:%M:%S.%f%z')
dateTime = dateTime.strftime("%a %d-%b-%y, %H:%M UTC")

template = Template(open('Covid-19_Dashboard/Covid-19_SVG_Template.svg').read())
out = template.render(Country=_Country, State=_State, index=str(_index[-1]), data_c=f"{int(Confirmed[0][-1]):,d}",
                      data_r=f"{int(Recovered[0][-1]):,d}",
                      data_d=f"{int(Deaths[0][-1]):,d}",
                      dateTime=dateTime)

with open("Covid-19_Dashboard/Covid-19.svg", "w") as outfile:
    outfile.write(out)
