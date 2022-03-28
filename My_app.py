import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(page_title='IGS Results')
st.title("INFORMATION GAPS STUDY")
st.header('IGS Results Senegal')


image = Image.open('LIFFT.png')

st.image(image)

st.markdown("# The database")
df = pd.read_excel("IGS.xlsx")
st.write(df)

# General and occupation
st.markdown("# General and occupation")
df1=df.iloc[:,0:9]


for i in df1.columns:
    fig = px.histogram(df1, x = i, color_discrete_sequence=['#EF553B'])
    st.plotly_chart(fig)

# IT Assets and Connectivity
st.markdown("# IT Assets and Connectivity")
df2=df.iloc[:,10:44]

for i in df2.columns:
    fig1 = px.histogram(df2, x = i, color_discrete_sequence=['#EF553B'])
    st.plotly_chart(fig1)


# Available information
st.markdown("# Available informations")
df3=df.iloc[:,45:78]

for i in df3.columns:
    fig2 = px.histogram(df3, x = i, color_discrete_sequence=['#EF553B'])
    st.plotly_chart(fig2)


# Gaps information
st.markdown("# Gaps informations")
df4=df.iloc[:,95:110]

for i in df4:
    fig3 = px.histogram(df4, x = i, color_discrete_sequence=['#EF553B'])
    st.plotly_chart(fig3)