import streamlit as st

from libraries.database_management import connect_mongo

st.header('Registrera ny vara')

# collection = connect_mongo.connect_to_a_mongo()

# mydic = {
#     'deal': {
#         'product': 'Bregott 600 g',
#         'pris': '39kr',
#         'butik': 'Ica Oj Söder'
#     }}

# collection.insert_one(mydic)

# findings = collection.find()
# st.write(findings)

register = st.form()
register.input