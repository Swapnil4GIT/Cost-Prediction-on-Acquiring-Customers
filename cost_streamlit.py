import streamlit as st
import pandas as pd
import datetime
import graphviz
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import plotly.express as px


# Heading of the project
st.write(
    """
    ## Cost Prediction on acquiring Customers
    ###### Cost to run a media campaign for US FoodMarts according to Income, Store Data
    """
)

st.write(
    """
    ***
    """
)

st.write(
    """
    <p style="font-size: 20px;">
    <b>About FoodMart</b>
    </p>
     """, unsafe_allow_html=True
)

# About the FoodMart Company
col1, col2 = st.columns(2, gap='large')

with col1:
    st.markdown(
        """
        
        <p style="font-size: 15px;">
        Food Mart (CFM) is a chain of convenience stores in the United States. The private company's headquarters are located in Mentor, Ohio and
        there are currently approximately 325 stores located in the United States. Convenient Food Mart operates on the franchise system.
        </p>
        """, unsafe_allow_html=True
    )
 
with col2:
    st.markdown(
        """
        <p style="font-size: 15px;">
        Food Mart was the nation's third-largest chain of convenience stores as of 1988. The NASDAQ exchange dropped Convenient Food Mart the same
        year when the company failed to meet financial reporting requirements. Carden & Cherry advertised Convenient Food Mart with the Ernest
        character in the 1980s
        </p>
        """, unsafe_allow_html=True
    )
 
#Problem statements and value propositions

col1,col2 = st.columns([2,3], gap='large')

with col1:
    st.write(
        """
        ***
        """
    )
    st.markdown(
        """
        <p style="font-size: 20px;">
        <b>Problem Statement</b>
        </p>
        """, unsafe_allow_html=True
    )
    st.markdown(
        """
        <p style="font-size:15px;">
        Predict the accurate cost of running media campaign subject to different market conditions based on the historical data.
        Explore media campaign running cost in advance to acquire new customers and give an edge to the company in making business decisions.
        </p>
        """, unsafe_allow_html=True
    )
    st.image("./Images/Questionmark.jpg")

#Data description

with col2:
    st.write(
        """
        ***
        """
    )
    st.markdown(
        """
        <p style="font-size: 20px;">
        <b>Data Quality Analysis</b>
        </p>
        """, unsafe_allow_html=True
    )
    st.markdown(
        """
        <ul>
            <li>
                <p style="font-size:15px;">
                Available data volume of around 60K customers which were acquired in the past. The data contains their acquisition cost too
                </p>
            </li>
            <li>
                <p style="font-size:15px;">
                Shape of data is 60428 * 40 i.e. the given dataset has 60428 rows and 40 columns
                </p>
            </li>
            <li>
                <p style="font-size:15px;">
                There is no data point missing across all the features from the given dataset
                </p>
            </li>
            <li>
                <p style="font-size:15px;">
                Available data types of features from the given dataset - Discrete numeric/non-numeric & Continuous numeric
                </p>
            </li>
            <li>
                <p style="font-size:15px;">
                Total marketing cost of acquiring customers is approx. $60 million/year.
                This is the consolidate customer acquisition cost for all the customers from the dataset.
                </p>
            </li>
            <li>
                <p style="font-size:15px;">
                Target variable identified here is the cost of acquiring a customer.​
               </p>
            </li>
        </ul>
        </p>
        """, unsafe_allow_html=True
    )

# Read DataFrame
st.write("#")
st.write("#")
st.write(
    """
    <p style="font-size: 20px;">
    <b>DataFrame</b>
    </p>
     """, unsafe_allow_html=True
)

df = pd.read_csv('./Data/media prediction and its cost.csv')
st.write(df.head(10))

#EDA
#Tree chart
st.write("#")
st.write("#")

st.write(
    """
    <p style="font-size: 20px;">
    <b>Exploratory Data Analysis</b>
    </p>
     """, unsafe_allow_html=True
)

st.image("./Images/EDA.png", caption="Data Grouped at Different Levels", output_format="auto")

st.write("#")
st.write(
    """
    <p style="font-size: 20px;">
    <b>Features <i> w.r.t </i> acquired customers and CAC</b>
    </p>
     """, unsafe_allow_html=True
)

st.write(
    """
    <p style="font-size: 17px;">
    Feature : Promotion Names
    </p>
     """, unsafe_allow_html=True
)

col1, col2 = st.columns(2, gap='small')

with col1:
    st.write(
    """
    <p style="font-size: 17px;">
    Customers Acquired
    </p>
     """, unsafe_allow_html=True
    )
    st.image("./Images/promopie.png")

with col2:
    st.write(
    """
    <p style="font-size: 17px;">
    CAC Spread
    </p>
     """, unsafe_allow_html=True
    )
    st.image("./Images/promobox.png")

#----
st.write("#")
st.write(
    """
    <p style="font-size: 17px;">
    Feature : Media Type
    </p>
     """, unsafe_allow_html=True
)

col1, col2 = st.columns(2, gap='small')

with col1:
    st.write(
    """
    <p style="font-size: 17px;">
    Customers Acquired
    </p>
     """, unsafe_allow_html=True
    )
    st.image("./Images/mediatypepie.png")

with col2:
    st.write(
    """
    <p style="font-size: 17px;">
    CAC Spread
    </p>
     """, unsafe_allow_html=True
    )
    st.image("./Images/mediatypebox.png")
