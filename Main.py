# INF601 - Advanced Programming in Python
# Janelyn Nichols
# Final Project

import altair as alt
import pandas as pd
import streamlit as st
import requests
import bs4

df = pd.read_csv('tyson lot 4.2.24 - 4.30.24.csv') # data source .csv file
#print(df.to_string())

st.title('Lots Harvested at Tyson During April') #Steamlit site title
#st.write(df)

st.sidebar.header('Options') #sidebar information
option = st.sidebar.selectbox('Which Dashboard would you like to use?', ('Kill Date', 'Supplier', 'Weather at the Plant'))

st.header(option)

if option == 'Kill Date': #Kill date dashboard
    st.subheader('April Tyson Kills by Date')


    def get_tyson_data():
        df = pd.read_csv('Tyson Lot 4.2.24 - 4.30.24.csv')
        return df.set_index('KILL DATE') #Kill date index
    try:
        df=get_tyson_data()
        supplier = st.multiselect('Choose Kill Date', list(df.index), ['4/30/2024'])
        if not supplier:
            st.error('Please select at least one date.')
        else:
            data = df.loc[supplier]
            st.write("April Tyson Kills by Date", data.sort_index())

            data = data.T.reset_index()
            data = pd.melt(data, id_vars=['index']).rename(columns={'index': 'Supplier Name', 'value': 'Kill Date'}
            )
            chart = (
                alt.Chart(data)
                .mark_area(opacity=0.3)
                .encode()
                 )
    except EOFError as e: st.error( "This demo requires internet access. Please try again later.")

if option == 'Supplier': #Supplier dashboard
    st.subheader('April Tyson Kills by Supplier')

    def get_tyson_data():
        df = pd.read_csv('Tyson Lot 4.2.24 - 4.30.24.csv')
        return df.set_index('SUPPLIER') #Supplier index
    try:
        df=get_tyson_data()
        supplier = st.multiselect('Choose Supplier', list(df.index), [129413])
        if not supplier:
            st.error('Please select at least one supplier.')
        else:
            data = df.loc[supplier]
            st.write("April Tyson Kills by Supplier", data.sort_index())

            data = data.T.reset_index()
            data = pd.melt(data, id_vars=['index']).rename(columns={'index': 'Supplier Name', 'value': 'Kill Date'}
            )
            chart = (
                alt.Chart(data)
                .mark_area(opacity=0.3)
                .encode()
                 )
    except EOFError as e: st.error( "This demo requires internet access. Please try again later.")

if option == 'Weather at the Plant': #Current weather at Tyson plant dashboard
    pass

    r = requests.get('https://forecast.weather.gov/MapClick.php?lat=37.9891&lon=-100.9882')

    weather = bs4.BeautifulSoup(r.text, 'html.parser')

    elems = weather.select('#current_conditions_detail')

    st.write(elems[0].getText())


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