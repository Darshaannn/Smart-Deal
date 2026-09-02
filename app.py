import streamlit as st 
import joblib

st.title("Samrt Deal")

st.write("AI-Assisted Used Car Price & Deal Intelligence")

bundle=joblib.load("smartdeal_bunddle.joblib")

model=bundle["model"]
tolerance =model["tolerance "]
features=bundle["features"]
