
# Import libraries

import streamlit as st
import pandas as pd
import joblib

# Load our Model Pipeline Object
model = joblib.load('sales_predictor_model.joblib')

# add title and instructions
st.title('Video Game Global Sales Predictor')
st.subheader('Enter Game information and submit for likely sales (in Millions)')

# age input form

Year = st.number_input(
    label = '01. Enter the Year of Release',
    min_value = 1980,
    max_value = 2050,
    value = 2026
    )

# gender input form

Publisher = st.text_input(
    '02. Enter the Game\'s Publisher'
    )


# credit score input form

Platform = st.radio(
    label = '03. Enter the Platform the Game will be on',
    options = ['PS4', 'XOne', 'PC']
    )

# Genre input

Genre = st.text_input(
    '04. Enter the Game Genre'
    )


# submit inputs to model

if st.button('Submit for Prediction'):
    
    # store our Data in a Data Frame for prediction
    new_data = pd.DataFrame({'Year' : [Year], 'Publisher' : [Publisher], 'Platform' : [Platform], 'Genre' : [Genre]})
    
    # apply model pipeling to the input data and extract probability prediction
    pred = model.predict(new_data)
    
    # output prediction
    st.subheader(f'Based on these game attributes, our model predicts a likely sales of {pred} (Million)')



















