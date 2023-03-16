import streamlit as st
import pandas as pd
import datetime

# Heading of the project
st.write(
    """
    ## Cost Prediction on acquiring Customers
    ###### Cost to run a media campaign for US FoodMarts according to Income, Store Data
    """
)

# About the FoodMart Company
col1, col2 = st.columns([3,2])

with col1:
    st.markdown(
        """
        <p style="font-size: 18px;">
        About FoodMart
        </p>
        """, unsafe_allow_html=True
    )
    st.markdown(
        """
        
        <p style="font-size: 15px;">
        Food Mart (CFM) is a chain of convenience stores in the United States. The private company's headquarters are located in Mentor, Ohio and
        there are currently approximately 325 stores located in the United States. Convenient Food Mart operates on the franchise system.
        Food Mart was the nation's third-largest chain of convenience stores as of 1988. The NASDAQ exchange dropped Convenient Food Mart the same
        year when the company failed to meet financial reporting requirements. Carden & Cherry advertised Convenient Food Mart with the Ernest
        character in the 1980s
        </p>
        """, unsafe_allow_html=True
    )