import streamlit as st
import pandas as pd
import numpy as np
from joblib import load

def word(password):
    character=[]
    for i in password:
        character.append(i)
    return character

model_pipeline = load('model.joblib')

st.title('Password Strength Checker App')
st.write('This app predicts the strength of a password as strong, medium, or weak.')

password = st.text_input('Enter a password:', type='password')

if st.button('Predict'):

    prediction = model_pipeline.predict([password])
    result = prediction[0]

    if result == 'Weak':
        st.error('The password is: Weak')
    elif result == 'Medium':
        st.warning('The password is: Medium')
    else:
        st.success('The password is: Strong')