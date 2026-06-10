import streamlit as st
from openai import OpenAI

# Load API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("Commodity Code Finder")

description = st.text_area("Enter product description:")

if st.button("Find Code"):
    prompt = f"""
    You are a customs expert.
    Based on the description below, suggest the most likely HS commodity code and explain why.

    Description: {description}

    Answer format:
    - Code:
    - Description:
    - Reason:
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    st.write(response.choices[0].message.content)
