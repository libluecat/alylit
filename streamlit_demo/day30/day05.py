# -*- coding:utf-8 -*-
"""
作者：BlueCat
日期：2023年09月04日
"""
import numpy as np
import pandas as pd
import streamlit as st
import altair as alt

# 大标题
st.header('st.write')

# 显示文字
st.subheader('Display Text')
st.write('Hello,World! :sunglasses:')

# 显示数字
st.subheader('Display Numbers')
st.write(1234)

# 显示dataframe
st.subheader('Display DataFrame')
df = pd.DataFrame(data={
    'first_col': [1, 2, 3, 4],
    'second_col': [5, 6, 7, 8]
})
st.write(df)

# 同时显示文字和dataframe
st.subheader('Accept multiple arguments')
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# 显示图表
st.subheader('Display charts')
df_chart = pd.DataFrame(data=np.random.randn(200, 3), columns=list('abc'))
alt_chart = alt.Chart(data=df_chart).mark_circle().encode(x='a', y='b', size='c', color='c', tooltip=list('abc'))

st.write(alt_chart)
