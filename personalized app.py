# -*- coding: utf-8 -*-
"""
Created on Fri Apr 25 22:17:32 2025

@author: user
"""

import streamlit as st

# Title of the App
st.title("Personalized Compliment App")

# Ask the User for Their Name
user_name = st.text_input("Enter your name:")

# Display Personalized Message
if user_name:
    st.markdown(f"""
    <div style="text-align: center; margin-top: 50px;">
        <h1 style="color: #FF69B4;">{user_name}, You Are Beautiful! 💖</h1>
    </div>
    """, unsafe_allow_html=True)