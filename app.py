import streamlit as st
import pandas as pd

from libraries.database_management import connect_mongo

st.header('Registrera ny vara')

collection = connect_mongo.connect_to_a_mongo()

mydic = {
    'deal': {
        'product': 'Bregott 600 g',
        'pris': '39kr',
        'butik': 'Ica Oj Söder'
    }}

collection.insert_one(mydic)

findings = collection.find()
st.write(findings)

register = st.form('key')
col1, col2, col3 = st.columns([3,1,3], vertical_alignment='bottom')
with col1:
    register.text_input("Vara")
with col2:
    register.text_input("Pris")
with col3:
    register.text_input('Butik')

register.form_submit_button('skicka')