# -*- coding:utf-8 -*-
"""
作者：BlueCat
日期：2023年09月04日
"""
import numpy as np
import pandas as pd
import streamlit as st

st.header("Line Chart")
df = pd.DataFrame(data=np.random.randn(20, 3), columns=list('abc'))
st.line_chart(data=df)
