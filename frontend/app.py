import streamlit as st
import requests

FASTAPI_URL = "https://shl-rag-assignment.onrender.com/"  # your deployed backend

st.title("SHL Assessment Recommender")

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
            results = response.json().get("results", [])
            if results:
                st.success("Results loaded!")
                for result in results:
                    st.write(f"**{result.get('name', 'Untitled')}**")
                    st.write(result.get("description", "No description available."))
                    st.write(f"Duration: {result.get('duration')} minutes")
                    st.write(f"Remote Support: {result.get('remote_support')}")
                    st.write(f"Adaptive: {result.get('adaptive')}")
                    st.markdown(f"[More Info]({result.get('url')})")
                    st.markdown("---")
            else:
                st.warning("No results found.")
        else:
            st.error("Something went wrong fetching data.")
