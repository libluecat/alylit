# -*- coding:utf-8 -*-
"""
作者：BlueCat
日期：2023年09月04日
"""
import streamlit as st
import numpy as np
from datetime import time, datetime

st.header('st.slider')

st.subheader('Slider')
slider_num = st.slider(label='How old are you?', min_value=0, max_value=130, value=25)
st.write(f"I'm {slider_num} years old")

st.subheader('Range slider')
values = st.slider(label='Select a range of values', min_value=0.0, max_value=100.0, value=(25.0, 75.0))
st.write(f'Values:{values}')

st.subheader('Range time slider')
appointment = st.slider(label='Schedule your appointment:', value=(time(11, 30), time(12, 45)))
st.write(f"You're scheduled for::{appointment}")

st.subheader('Datetime slider')
star_time = st.slider(label='When do you start?', min_value=datetime(2019, 12, 18, 9, 30),
                      max_value=datetime(2020, 1, 15, 9, 30), value=datetime(2020, 1, 1, 9, 30),
                      format='yyyy-MM-dd hh:mm:ss')
st.write(f'Start time: {star_time}')
