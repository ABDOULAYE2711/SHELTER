import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(page_title='IGS Results')
st.title("INFORMATION GAPS STUDY")
st.header('IGS Results Senegal')


#----write Image--------
image = Image.open('LIFFT.png')

st.image(image)

#----write Dataframe--------
st.markdown("# The database")
df = pd.read_excel("IGS1.xlsx")


#----FILTER--------
st.sidebar.header("Please Filter Here :")
organization = st.sidebar.multiselect(
    "Select the Organization:",
    options=df['Type_of_Organization'].unique(),
    default=df['Type_of_Organization'].unique()
)


country = st.sidebar.multiselect(
    "Select the Country:",
    options=df['Country'].unique(),
    default=df['Country'].unique()
)

df_select = df.query(
    "Type_of_Organization == @organization & Country == @country"
)

st.dataframe(df_select)

# General and occupation
st.markdown("# General and occupation")
df1=df_select.iloc[:,0:10]


for i in df1.columns:
    fig = px.histogram(df1, x = i, color_discrete_sequence=['#EF553B'])
    st.plotly_chart(fig)

# IT Assets and Connectivity
st.markdown("# IT Assets and Connectivity")
df2=df_select.iloc[:,11:45]

for i in df2.columns:
    fig1 = px.histogram(df2, x = i, color_discrete_sequence=['#EF553B'])
    st.plotly_chart(fig1)


# Available information
st.markdown("# Available informations")
df3=df_select.iloc[:,46:79]

for i in df3.columns:
    fig2 = px.histogram(df3, x = i, color_discrete_sequence=['#EF553B'])
    st.plotly_chart(fig2)


# Gaps information
st.markdown("# Gaps informations")
df4=df_select.iloc[:,80:95]

for i in df4:
    fig3 = px.histogram(df4, x = i, color_discrete_sequence=['#EF553B'])
    st.plotly_chart(fig3)
