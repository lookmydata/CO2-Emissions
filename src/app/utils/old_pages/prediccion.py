import streamlit as st
from utils.KPI2030_ML import MLKPI
from darts import TimeSeries

df=MLKPI.getDataframe()
series = TimeSeries.from_dataframe(df,time_col='date',value_cols='smoothed')
st.write(MLKPI.getForecast())
