import streamlit as st
import requests

FASTAPI_URL = "https://shl-rag-assignment.onrender.com/"  # your deployed backend

st.title("SHL Assessment Recommender")

query = st.text_input("Enter job role or keywords:")

if st.button("Search") and query:
    with st.spinner("Fetching recommendations..."):
        response = requests.post(f"{FASTAPI_URL}/recommend", json={"query": query})

        if response.status_code == 200:
            results = response.json()
            st.success("Results loaded!")

            for result in results:
                st.write(f"**{result['title']}**")
                st.write(result.get("description", "No description available."))
                st.markdown("---")
        else:
            st.error("Something went wrong fetching data.")
