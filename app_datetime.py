import streamlit as st
import datetime

d = st.date_input("when's your birthday", datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)

t = st.time_input('Set an alarm for', datetime.time(8, 45))
st.write('Alarm is set for', t)