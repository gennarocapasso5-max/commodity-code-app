import streamlit as st

st.title("Commodity Code Finder")

description = st.text_area("Enter product description:")

if st.button("Find Code"):
    st.write("This is where the code result will appear.")
``
