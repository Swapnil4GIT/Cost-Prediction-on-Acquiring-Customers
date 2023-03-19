import streamlit as st
import pandas as pd
import datetime
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

st.write(
    """
    ***
    """
)

st.write(
    """
    <p style="font-size: 20px;">
    <b>Feature Encoding</b>
    </p>
     """, unsafe_allow_html=True
)
st.markdown(
"""
<p style="font-size:15px;">
We discovered during EDA that our dataset doesn't show linear behaviour when we analyzed and looked at
the correlation map and relationship of target variable with various other continuous features. So We are
aiming for the Tree Based model. After performing the one-hot encoding of the categorical variables we are arrived
at the dataset of <i>60K * 214</i>.
</p>
""", unsafe_allow_html=True
)
st.write(
    """
    ***
    """
)
#--
st.write(
    """
    <p style="font-size: 20px;">
    <b>Model building</b>
    </p>
     """, unsafe_allow_html=True
)
st.markdown(
"""
<p style="font-size:15px;">
Since we are going to use the tree based machine learning model, we will first try with bagging approach where we will try
to reduce the variance of individual tree by bootstrap aggregration.
</p>
""", unsafe_allow_html=True
)
st.write('#')
st.write(
    """
    <p style="font-size: 18px;">
    <b>Random Forest Regressor</b>
    </p>
     """, unsafe_allow_html=True
)
st.markdown(
"""
<p style="font-size:15px;">
Results of RandomForestRegressor are too good to believe and that raised the concern of overfitting. The parameters and the corresponding
model evaluation results are mentioned for after hypertunning with different estimators and tree depth. During hypertunning it is observed that
increasing the number of estimators was not adding much value to the improvement of the model. However maximizing the tree depth was giving much 
better results. However with the depth of <i>max_depth=5</i> and maximum estimators of <i>n_estimators=500</i> didn't gave any promising results.
</p>
""", unsafe_allow_html=True
)
col1,col2 = st.columns(2, gap='large')
with col1:
    st.write(
    """
    <p style="font-size: 15px;">
    <b>Default parameters</b>
    </p>
     """, unsafe_allow_html=True
    )
    st.image("./Images/defaultRFR.png")

with col2:
    st.write(
    """
    <p style="font-size: 15px;">
    <b>Model Performance</b>
    </p>
     """, unsafe_allow_html=True
    )    
    st.markdown(
    """
    <p style="font-size:15px;">
    MAE  :  0.052, 
    RMSE :  0.777, 
    MAPE :  0.0, 
    R2   :  0.999\n
    This model performance on test dataset is too good to believe. Upong further analysis, it is observed that since this is the model with 
    default parameters, it used the default <i>max_depth</i> parameter which resulted in such a surprising results.
    </p>
    """, unsafe_allow_html=True
    )
#--
st.write('#')
st.write(
    """
    <p style="font-size: 18px;">
    <b>Hyperparameter Tuning</b>
    </p>
     """, unsafe_allow_html=True
)
st.markdown(
"""
<p style="font-size:15px;">
Let's perform hyperparameter tuning on the model where the goal is to keep the number of estimators realistic and max depth should be sensible too.
Hence upong doing further tuning with grid serach algorithm. 
</p>
""", unsafe_allow_html=True
)
col1,col2 = st.columns(2, gap='large')
with col1:
    st.write(
    """
    <p style="font-size: 15px;">
    <b>Sensible parameters</b>
    </p>
     """, unsafe_allow_html=True
    )
    st.image("./Images/sensibleRFR.png")

with col2:
    st.write(
    """
    <p style="font-size: 15px;">
    <b>Model Performance</b>
    </p>
     """, unsafe_allow_html=True
    )    
    st.markdown(
    """
    <p style="font-size:15px;">
    Here is the tricky part. If we want to keep the tree max_depth sensible then the observed parameter score is quite bad. Another observed phenomenon 
    here is that increasing the number of estimators is not adding any value to the model performance. This makes rise to the thought of checking
    on the input data's sparsity percentage and if there is any impact on the model performance due to sparse features.
    </p>
    """, unsafe_allow_html=True
    )

#--
st.write('#')
st.write(
    """
    <p style="font-size: 18px;">
    <b>Sparsity Control</b>
    </p>
     """, unsafe_allow_html=True
)
st.markdown(
"""
<p style="font-size:15px;">
We noticed that the RandomForest Regressor is not able to learn the features properly and gave the accuracy
as bad as 11% even after doing the hypertuning. We again noticed that if the depth of the tree increases then
the model performance also goes up. This could very well be due to the sparse features created after one-hot 
encoding. We are going to look at the sparse features and how their model performance gets affected with the
different percentages of the sparsity in the data. 
</p>
""", unsafe_allow_html=True
)
col1,col2 = st.columns(2, gap='large')
with col1:
    st.write(
    """
    <p style="font-size: 15px;">
    <b>Sparsity Control Graph</b>
    </p>
     """, unsafe_allow_html=True
    )
    st.image("./Images/sparsitycontrol.png")

with col2:
    st.write(
    """
    <p style="font-size: 15px;">
    <b>Observations</b>
    </p>
     """, unsafe_allow_html=True
    )    
    st.markdown(
    """
    <p style="font-size:15px;">
    We can notice that, sparse featues at 10%, 20% and 30% are causing no change to the model performance.
    Also on the upper side we can notice that sparse features at 70% and 80% having almost same accuracy.
    This gives the feeling of trying to make the dataset more dense and re-build the model and evaluate the
    performance.
    </p>
    """, unsafe_allow_html=True
    )

#--
st.write('#')
st.markdown(
"""
<p style="font-size:15px;">
To reduce the sparsity, we tried target encoding followed by binning which then followed by one-hot-encoding.
This has brought down the dataset dimensionality from 214 to 116. With this less sparse data, the RandomForestRegressor
could achieve the accuracy of 30% which is quite an improvement over the previous model with R2 of 11%. But still the model is off by
70% which means the model couldn't learn the features correctly. 
</p>
""", unsafe_allow_html=True
)

st.write(
    """
    ***
    """
)
#--
st.write(
    """
    <p style="font-size: 20px;">
    <b>Boosting : GradientBoostingRegressor</b>
    </p>
     """, unsafe_allow_html=True
)
st.markdown(
"""
<p style="font-size:15px;">
Since bagging approach couldn't learn the features properly we are shifting towards boosting technique where bias will be reduced instead of variance.
We are going to try the GradientBoostingRegressor model where our aim will be to achieve the good accuracy with reasonable parameters and reasonable
training time. 
</p>
""", unsafe_allow_html=True
)
st.write('#')
st.markdown(
"""
<p style="font-size:15px;">
Hyperparameter tuning with different learning rates and different number of estimators. 
</p>
""", unsafe_allow_html=True
)
st.image("./Images/gbctuning.png")

st.write('#')
st.markdown(
"""
<p style="font-size:15px;">
Train vs Test accuracy. 
</p>
""", unsafe_allow_html=True
)
st.image("./Images/gbrtrainvstest.png")

st.write('#')
st.markdown(
"""
<p style="font-size:15px;">
Error vs n_estimators. 
</p>
""", unsafe_allow_html=True
)
st.image("./Images/errorvsestimators.png")

st.write('#')
st.markdown(
"""
<p style="font-size:15px;">
Actual vs Predicted values scatterplot. 
</p>
""", unsafe_allow_html=True
)
st.image("./Images/actualvspredicted.png")

st.write('#')
col1,col2 = st.columns(2, gap='large')
with col1:
    st.write(
    """
    <p style="font-size: 15px;">
    <b>Sensible/Best parameters</b>
    </p>
     """, unsafe_allow_html=True
    )
    st.image("./Images/gbrscores.png")

with col2:
    st.write(
    """
    <p style="font-size: 15px;">
    <b>Model Performance</b>
    </p>
     """, unsafe_allow_html=True
    )    
    st.markdown(
    """
    <p style="font-size:15px;">
    The model performance on hyperparameter tuning clearly shows us that we can either keep the learning rate high or n_estimators as high. 
    Since we want to avoid the overfitting chance although gradient boosting are considered as robust to overfitting, we chose to have less
    number of estimators and high learning rate. We observed that the high learning rate is not causing the overshoot issue and learning rate
    is not a subject to overfitting issue.
    </p>
    """, unsafe_allow_html=True
    )

st.write(
    """
    ***
    """
)

st.caption(
    """
    Interactive app building based on best model is in progress . . . . .
    """
)