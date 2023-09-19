import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv("happy.csv")

happiness_df = df["happiness"]
gdp_df = df["gdp"]
generosity_df = df["generosity"]

st.header("In Search for Happiness")

x = st.selectbox("Select the data for the X-Axis",
                 ("Happiness", "GDP", "Generosity"))
y = st.selectbox("Select the data for the Y-Axis",
                 ("Happiness", "GDP", "Generosity"))

st.subheader(f"{x} and {y}")

match x:
    case "Happiness":
        x_axis = happiness_df
    case "GDP":
        x_axis = gdp_df
    case "Generosity":
        x_axis = generosity_df

match y:
    case "Happiness":
        y_axis = happiness_df
    case "GDP":
        y_axis = gdp_df
    case "Generosity":
        y_axis = generosity_df

fig = px.scatter(x=x_axis, y=y_axis)
fig.update_layout(xaxis_title=x, yaxis_title=y)
st.plotly_chart(fig)
