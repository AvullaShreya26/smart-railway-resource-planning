import streamlit as st
import pandas as pd

df = pd.read_csv("railway_data.csv")

st.title("Smart Railway Resource Planning")

st.write(df)

st.subheader("Passenger Demand by Route")
st.bar_chart(df.groupby("Route")["Passenger_Count"].sum())

st.subheader("Platform Usage")
st.bar_chart(df["Platform_Number"].value_counts())
