import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(page_title="Commodity Code Finder", layout="centered")

st.title("Commodity Code Finder")
st.markdown("Search for the correct HS (commodity) code")

# Load CSV
df = pd.read_csv("hs_codes.csv")

# Clean column names
df.columns = df.columns.str.lower()

# Try to automatically detect columns
if "description" not in df.columns:
    df["description"] = df.iloc[:, 1]

if "code" not in df.columns:
    df["code"] = df.iloc[:, 0]

# User input
search = st.text_input("Enter product description")

# Search logic
if search:
    results = df[df["description"].astype(str).str.contains(search, case=False, na=False)]

    if not results.empty:
        st.subheader("Top Matches")
        st.dataframe(results[["code", "description"]].head(10))
    else:
        st.warning("No matches found. Try different keywords.")

# Info
st.info("This is a free version using dataset matching. Always verify codes before use.")
