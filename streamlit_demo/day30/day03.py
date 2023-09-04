# -*- coding:utf-8 -*-
"""
作者：BlueCat
日期：2023年09月04日
"""
import streamlit as st

st.header("st.button")

if st.button("Say Hello"):
    st.write("Why Hello there?")
else:
    st.write("Goodbye")
