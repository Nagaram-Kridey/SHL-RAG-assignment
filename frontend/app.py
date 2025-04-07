import streamlit as st
import requests

FASTAPI_URL = "https://shl-rag-assignment.onrender.com/"  # your deployed backend

st.title("SHL Assessment Recommender")

# Update button triggers the backend to scrape and update data
if st.button("🔄 Update Assessment Data"):
    with st.spinner("Updating data..."):
        try:
            response = requests.post(f"{FASTAPI_URL}/update-data")
            if response.status_code == 200:
                st.success("✅ Data updated successfully!")
            else:
                st.error(f"❌ Failed to update: {response.status_code}")
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

query = st.text_input("Enter job role or keywords:")

if st.button("Search") and query:
    with st.spinner("Fetching recommendations..."):
        response = requests.post(f"{FASTAPI_URL}/recommend", json={"query": query})

        if response.status_code == 200:
            results = response.json()
            st.success("Results loaded!")
            st.json(results)

            for result in results:
                st.write(f"**{result.get('name', 'Untitled')}**")
                st.write(result.get("description", "No description available."))
                st.markdown("---")
        else:
            st.error("Something went wrong fetching data.")
