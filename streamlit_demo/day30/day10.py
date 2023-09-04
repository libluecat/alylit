# -*- coding:utf-8 -*-
"""
作者：BlueCat
日期：2023年09月04日
"""
import streamlit as st

st.header('st.selectbox')

favorite_color = st.selectbox(label='What is your favorite color?', options=['Blue', 'Green', 'Red'])
st.write(f'Your favorite color is {favorite_color}')
