# INF601 - Advanced Programming in Python
# Janelyn Nichols
# Final Project
import altair
import pandas as pd
import streamlit as st

df = pd.read_csv('tyson lot 4.2.24 - 4.30.24.csv')
#print(df.to_string())

st.title('Lots Harvested at Tyson During April')
st.write(df)

def get_tyson_data():
    df = pd.read_csv('Tyson Lot 4.2.24 - 4.30.24.csv')
    return df.set_index('SUPPLIER')
try:
    df=get_tyson_data()
    supplier = st.multiselect('Choose Supplier', list(df.index), [129413])
    if not supplier:
        st.error('Please select at least one supplier.')
    else:
        data = df.loc[supplier]
        st.write("###April Tyson Kills by Yard", data.sort_index())

        data = data.T.reset_index()
        data = pd.melt(data, id_vars=['index']).rename(columns={'index': 'Supplier Name', 'value': 'Kill Date'}
        )
        chart = (
            alt.Chart(data)
            .mark_area(opacity=0.3)
            .encode()
             )
except EOFError as e: st.error( "This demo requires internet access. Please try again later.")



"""
df = pd.read_csv('Tyson Lot 4.2.24 - 4.30.24.csv')
st.line_chart(df)

def get_tyson_data():
    df = pd.read_csv('Tyson Lot 4.2.24 - 4.30.24.csv')
    return df.set_index('SUPPLIER')

try:
    df = get_tyson_data()
    supplier = st.multiselect('Choose Supplier', list(df.index), [129413])
supplier = st.multiselect('Choose Supplier'), list(df['SUPPLIER'].unique())
    if not supplier:
        st.error('Please select at least one supplier.')
    else:
        data = df.loc[supplier]
        st.write("###April Tyson Kills by Yard", data.sort_index())

        data = data.T.reset_index()
        data = pd.melt(data, id_vars=['index']).rename(columns={'index': 'Supplier Name', 'value': 'Kill Date'}
        )
        chart = (
            alt.chart(data)
            .mark_area(opacity=0.3)
            .encode()
        )
except EOFError as e:
    st.error(
        "This demo requires internet access. Please try again later.")
"""