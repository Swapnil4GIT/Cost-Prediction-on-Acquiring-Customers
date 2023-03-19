import streamlit as st
import pandas as pd
import datetime
import graphviz
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import plotly.express as px
from PIL import Image

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

st.write(
    """
    ***
    """
)
col1, col2 = st.columns([2,0.01],gap='small')
with col1:
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
        
#Data description

st.write(
    """
    ***
    """
)
st.write(
    """
    <p style="font-size: 20px;">
    <b>Data Quality Analysis</b>
    </p>
    """, unsafe_allow_html=True
)
st.image("./Images/DQA.png", caption="Data Quality Analysis", output_format="auto")


# Read DataFrame
st.write(
    """
    ***
    """
)
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
    <p style="font-size: 18px;">
    <i>Feature</i> : Promotion Name
    </p>
     """, unsafe_allow_html=True
)

col1, col2 = st.columns(2, gap='small')

with col1:
    st.write(
    """
    <p style="font-size: 17px;">
    Observations
    </p>
     """, unsafe_allow_html=True
    )
    st.markdown(
    """
    <p style="font-size:15px;">
    Total Promotions from the dataset are 49.
    Most effective promos for customer acquisition are <i><u>Weekend Markdown</u></i> and 
    <i><u>Price Savers</u></i> with % acquisition of 3.86% and 3.84% respectively.
    CAC has good variability and distinctive spread under different campaign promos.
    Median CAC is above $2.5M and below $3.0M for most of the promos.
    \n\n
    Promo names with customer acquisition of 3 to 4 percent are -
    <i>Weekend Markdown, Two Day Sale, Price Savers, Price Winners, Save-It Sale, Super Duper Savers, Super Savers, One Day Sale </i>
    \n\n
    This gives us some sense that customers foot fall on weekend could be a catalyst in highest customer acquisition on
    <i>Weekend Markdown</i> promo.
    \n\n
    <i>Price Savers</i> promo seems to be quite popular among the customers as it is almost as effective as 
    <i>Weeken Markdown</i> promo.
    </p>
    """, unsafe_allow_html=True
    )

with col2:
    st.write(
    """
    <p style="font-size: 17px;">
    Customers Acquired
    </p>
     """, unsafe_allow_html=True
    )
    st.image("./Images/promopie.png")

    st.write(
    """
    <p style="font-size: 17px;">
    CAC Spread
    </p>
     """, unsafe_allow_html=True
    )
    st.image("./Images/promobox.png")

st.write(
    """
    ***
    """
)
#----
st.write("#")
st.write(
    """
    <p style="font-size: 18px;">
    <i>Feature</i> : Media Type
    </p>
     """, unsafe_allow_html=True
)

col1, col2 = st.columns(2, gap='small')

with col2:
    st.write(
    """
    <p style="font-size: 17px;">
    Observations
    </p>
     """, unsafe_allow_html=True
    )
    st.markdown(
    """
    <p style="font-size:15px;">
    Total media types from the given dataset are 13.
    Most effective media type for customer acquisition are Daily paper, Radio with % acquisition of 11.3%.
    CAC has good variability and distinctive spread under different media types.
    Median CAC is above $2.5M and below $3.0M for all media type.
    \n\n
    Media types with customer acquisition of 8 to 9 percent are - 
    <i>Product Attachment, Daily Paper/Radio/TV, Daily Paper, Street Handout, Radio, Sunday Paper</i> 
    \n\n
    Media types with customer acquisition of 6 to 7 percent are -
    <i>Instore coupon, Sunday Paper/Radio, Cash Register Handout</i>
    \n\n
    Media types with customer acquisition of 5 to 6 percent are -
    <i>TV, Bulk Mail, Sunday Paper/Radio/TV </i>
    </p>
    """, unsafe_allow_html=True
    )


with col1:
    st.write(
    """
    <p style="font-size: 17px;">
    Customers Acquired
    </p>
     """, unsafe_allow_html=True
    )
    st.image("./Images/mediatypepie.png")

    st.write(
    """
    <p style="font-size: 17px;">
    CAC Spread
    </p>
     """, unsafe_allow_html=True
    )
    st.image("./Images/mediatypebox.png")

st.write(
    """
    ***
    """
)
#--
st.write("#")
st.write(
    """
    <p style="font-size: 18px;">
    Correlation among Store Level Features
    </p>
     """, unsafe_allow_html=True
)

col1, col2 = st.columns(2, gap='small')

with col1:
    st.write(
    """
    <p style="font-size: 17px;">
    Observations
    </p>
     """, unsafe_allow_html=True
    )
    st.markdown(
    """
    <p style="font-size:15px;">
    Correlation between CAC (Customer Acquisition Cost) and Total Acquired Customers is non-linear.
    This is important observation to help us choose the correct machine learning model to automate the cost predict feature.
    \n\n
    CAC shows positive correlation (<u>But NOT Strong i.e. around 0.5</u>) with store unit sales, store sales and store cost.
    This makes us even more confident that the linear machine learning model would not give better results as far as store level features are concerned.
    </p>
    """, unsafe_allow_html=True
    )

with col2:
    st.write(
    """
    <p style="font-size: 17px;">
    CAC <i> vs </i>Customers Acquired
    </p>
     """, unsafe_allow_html=True
    )
    st.image("./Images/corrscatter.png")

    st.write(
    """
    <p style="font-size: 17px;">
    Corr. among variables at store level
    </p>
     """, unsafe_allow_html=True
    )
    st.image("./Images/corrheatmap.png")

st.write(
    """
    ***
    """
)
#--
st.write("#")
st.write(
    """
    <p style="font-size: 18px;">
    <i>Feature:</i> Food Category
    </p>
     """, unsafe_allow_html=True
)

col1, col2 = st.columns(2, gap='small')

with col2:
    st.write(
    """
    <p style="font-size: 17px;">
    Observations
    </p>
     """, unsafe_allow_html=True
    )
    st.markdown(
    """
    <p style="font-size:15px;">
    Total food categories from the input dataset are 45.
    Most effective food categories for customer acquisition are <i>Vegetables</i> and <i>Snack Foods</i> with % acquisition of 12.3% and 11.4%.
    CAC has good variability and distinctive spread under different food categories.
    Median CAC is above $2.5M and below $3.0M for almost all the food categories.
    \n\n
    Food categories with customer acquisition of 5 to 6 percent are -
    <i>Dairy, Meat, Food</i>
    \n\n
    Since <i>Vegetables, Snack Foods, Dairy, Meat, Fruit, Jam and Jellies</i> together contribute around 45% of total customers acquired,
    we can draw inference that grocery stores are important while doing promo campaigns.
    </p>
    """, unsafe_allow_html=True
    )

with col1:
    st.write(
    """
    <p style="font-size: 17px;">
    Customers Acquired
    </p>
     """, unsafe_allow_html=True
    )
    st.image("./Images/foodcatpie.png")

    st.write(
    """
    <p style="font-size: 17px;">
    CAC Spread
    </p>
     """, unsafe_allow_html=True
    )
    st.image("./Images/foodcatbox.png")

st.write(
    """
    ***
    """
)
#--
st.write("#")
st.write(
    """
    <p style="font-size: 18px;">
    <i>Feature:</i> Education
    </p>
     """, unsafe_allow_html=True
)

col1, col2 = st.columns(2, gap='small')

with col1:
    st.write(
    """
    <p style="font-size: 17px;">
    Observations
    </p>
     """, unsafe_allow_html=True
    )
    st.markdown(
    """
    <p style="font-size:15px;">
    Total education degrees from the input dataset are 5.
    Most effective educational degree for customer acquisition are <i>partial high school</i> 
    and <i>high school</i> with % acquisition of 30.1% and 29.5% respectively.
    CAC has similar variability and spread for both all education categories.
    Median CAC is above $2.5M and below $3.0M and is almost same for all education categories.
    \n\n
    We notice here that customer acquisition percentage falls as the level of education degree increases. We can draw few important inferences from this -
    such as either the customers acquired are teenagers or young customers under 18 or customers with higher education are less interested to become a
    registered customers by availing the promos. 
    </p>
    """, unsafe_allow_html=True
    )

with col2:
    st.write(
    """
    <p style="font-size: 17px;">
    Customers Acquired
    </p>
     """, unsafe_allow_html=True
    )
    st.image("./Images/educationpie.png")

    st.write(
    """
    <p style="font-size: 17px;">
    CAC Spread
    </p>
     """, unsafe_allow_html=True
    )
    st.image("./Images/educationbox.png")

st.write(
    """
    ***
    """
)
#--
st.write("#")
st.write(
    """
    <p style="font-size: 18px;">
    <i>Feature:</i> Member Card
    </p>
     """, unsafe_allow_html=True
)

col1, col2 = st.columns(2, gap='small')

with col2:
    st.write(
    """
    <p style="font-size: 17px;">
    Observations
    </p>
     """, unsafe_allow_html=True
    )
    st.markdown(
    """
    <p style="font-size:15px;">
    Total member cards type categories available in input dataset are 4.
    Most effective member card for customer acquisition is <i>Bronze</i> with % acquisition of 55.9%.
    CAC has different spread and variance for different member card.
    Median CAC is above $2.5M and below $3.0M for all categories of member cards.
    \n\n
    Out of the total customers acquired, 56% customers hold <i>Bronze Card</i>. This makes sense as not
    everyone can have more privileged cards and major section of the customers falls into an average category.
    </p>
    """, unsafe_allow_html=True
    )

with col1:
    st.write(
    """
    <p style="font-size: 17px;">
    Customers Acquired
    </p>
     """, unsafe_allow_html=True
    )
    st.image("./Images/membercardpie.png")

    st.write(
    """
    <p style="font-size: 17px;">
    CAC Spread
    </p>
     """, unsafe_allow_html=True
    )
    st.image("./Images/membercardbox.png")

st.write(
    """
    ***
    """
)
#--
st.write("#")
st.write(
    """
    <p style="font-size: 18px;">
    <i>Feature:</i> Occupation
    </p>
     """, unsafe_allow_html=True
)

col1, col2 = st.columns(2, gap='small')

with col1:
    st.write(
    """
    <p style="font-size: 17px;">
    Observations
    </p>
     """, unsafe_allow_html=True
    )
    st.markdown(
    """
    <p style="font-size:15px;">
    Total occupation categories from input data are 5.
    Most effective occupations for customer acquisition are <i>professional</i> and 
    <i>skilled manual</i> with % acquisition of 33% and 26.5% respectively.
    CAC has different spread and variance for different occupation.
    Median CAC is above $2.5M and below $3.0M for all categories of occupation.
    \n\n
    <i>Professional and Skilled Manual</i> together represents around 60% of total customers acquired.
    This gives us an inference that customers from working class community are not someone who can be ignored while deciding the campaign ads.
   </p>
    """, unsafe_allow_html=True
    )


with col2:
    st.write(
    """
    <p style="font-size: 17px;">
    Customers Acquired
    </p>
     """, unsafe_allow_html=True
    )
    st.image("./Images/occupationpie.png")

    st.write(
    """
    <p style="font-size: 17px;">
    CAC Spread
    </p>
     """, unsafe_allow_html=True
    )
    st.image("./Images/occupationbox.png")

st.write(
    """
    ***
    """
)
#--
st.write("#")
st.write(
    """
    <p style="font-size: 18px;">
    <i>Feature:</i> House Owner
    </p>
     """, unsafe_allow_html=True
)

col1, col2 = st.columns(2, gap='small')

with col2:
    st.write(
    """
    <p style="font-size: 17px;">
    Observations
    </p>
     """, unsafe_allow_html=True
    )
    st.markdown(
    """
    <p style="font-size:15px;">
    Total house owner categories from input dataset are 2. It's a binary feature.
    Most effective category for customer acquisition is houseowner customers with % acquisition of 60.4%.
    CAC has different spread and variance under different categories. Non-house owner has larger spread of CAC.
    Median CAC is above $2.5M and below $3.0M for houseowner and non-houseowner.
    \n\n
    It is an interesting perspective where we came to know how the customers acquired are distributed <i>w.r.t.</i> being houseowner.
   </p>
    """, unsafe_allow_html=True
    )

with col1:
    st.write(
    """
    <p style="font-size: 17px;">
    Customers Acquired
    </p>
     """, unsafe_allow_html=True
    )
    st.image("./Images/houseownerpie.png")

    st.write(
    """
    <p style="font-size: 17px;">
    CAC Spread
    </p>
     """, unsafe_allow_html=True
    )
    st.image("./Images/houseownerbox.png")

st.write(
    """
    ***
    """
)
#--
st.write("#")
st.write(
    """
    <p style="font-size: 18px;">
    <i>Feature:</i> Customer Salary
    </p>
     """, unsafe_allow_html=True
)

col1, col2 = st.columns(2, gap='small')

with col1:
    st.write(
    """
    <p style="font-size: 17px;">
    Observations
    </p>
     """, unsafe_allow_html=True
    )

    st.markdown(
    """
    <p style="font-size:15px;">
    Total income bins available from input dataset are 8.
    Most effective income bin for customer acquisition is 30K-50K with % acquisition of 32.3%
    CAC has different spread and variance under different income bins.
    Median CAC is above $2.5M and below $3.0M for all the income bins.
    \n\n
    Customer's income gives an interesting inference that lower income consumers have higher percentage of becoming registered customers.
    \n\n
    Customer's in the bin range of 10K-30K and 30K-50K together represents around 54% of total customers acquired in the past.
    </p>
    """, unsafe_allow_html=True
    )

with col2:
    st.write(
    """
    <p style="font-size: 17px;">
    Customers Acquired
    </p>
     """, unsafe_allow_html=True
    )
    st.image("./Images/incomepie.png")

    st.write(
    """
    <p style="font-size: 17px;">
    CAC Spread
    </p>
     """, unsafe_allow_html=True
    )
    st.image("./Images/incomebox.png")

st.write(
    """
    ***
    """
)
#--
st.write("#")
st.write(
    """
    <p style="font-size: 18px;">
    Correlation among Product Level Features
    </p>
     """, unsafe_allow_html=True
)

col1, col2 = st.columns(2, gap='small')

with col2:
    st.write(
    """
    <p style="font-size: 17px;">
    Observations
    </p>
     """, unsafe_allow_html=True
    )
    st.markdown(
    """
    <p style="font-size:15px;">
    Linear correlation is absent among the individual features.
    Dark green cells show strong positive correlation and dark brown shows strong negative correlation.
    Most of the dark green cells seen are the correlation with self. So, linear correlation is absent among the features.
    Correlation among numerical features is plotted and we can see that CAC has strong positive correlation with SRP i.e. Store Retail Price.
    Scatterplot between CAC and SRP shows clear heteroskedasticity although it is linear.
    This gives us an inference that a linear machine learning model will not work here and we may have to try non-linear ML models to predict the cost.
    </p>
    """, unsafe_allow_html=True
    )

with col1:
    st.write(
    """
    <p style="font-size: 17px;">
    Correlation map
    </p>
     """, unsafe_allow_html=True
    )
    st.image("./Images/productcorr.png")

    st.write(
    """
    <p style="font-size: 17px;">
    SRP <i> vs </i> CAC
    </p>
     """, unsafe_allow_html=True
    )
    st.image("./Images/SRPcaccorr.png")
