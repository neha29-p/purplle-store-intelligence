import streamlit as st

st.title("Purplle Store Intelligence")
st.write("Welcome to the retail analytics dashboard demo.")

# This button simulates running your analytics
if st.button("Run Analytics Analysis"):
    st.write("Processing CCTV data...")
    st.success("Analysis Complete! Detection results: 85% Occupancy.")
    st.balloons()