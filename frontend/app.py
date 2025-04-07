import streamlit as st
import requests

# Add custom CSS for better UI
st.markdown("""
    <style>
        body {
            background-color: #f4f7fc;
            color: #333;
            font-family: 'Arial', sans-serif;
        }

        .title {
            font-size: 2.5rem;
            font-weight: bold;
            color: #1f77b4;
            text-align: center;
        }

        .button {
            background-color: #1f77b4;
            color: white;
            padding: 10px 20px;
            border-radius: 5px;
            font-size: 1rem;
            transition: background-color 0.3s ease;
        }

        .button:hover {
            background-color: #0a5c8e;
        }

        .card {
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
            padding: 15px;
            transition: transform 0.3s ease-in-out;
        }

        .card:hover {
            transform: scale(1.05);
        }

        .card-header {
            font-size: 1.2rem;
            font-weight: bold;
            color: #1f77b4;
        }

        .card-body {
            margin-top: 10px;
            color: #555;
        }

        .card-footer {
            text-align: right;
            margin-top: 15px;
        }

        .spinner {
            font-size: 1.5rem;
            color: #1f77b4;
        }
    </style>
""", unsafe_allow_html=True)

# Add a title with more prominent styling
st.markdown('<div class="title">SHL Assessment Recommender</div>', unsafe_allow_html=True)

FASTAPI_URL = "https://shl-rag-assignment.onrender.com/"  # your deployed backend

if st.button("🔄 Update Assessment Data", key="update", help="Click to refresh the data from the backend"):
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

if st.button("Search", key="search", help="Search assessments based on your query"):
    with st.spinner("Fetching recommendations..."):
        response = requests.post(f"{FASTAPI_URL}/recommend", json={"query": query})

        if response.status_code == 200:
            results = response.json().get("results", [])
            if results:
                st.success("Results loaded!", icon="✅")
                for result in results:
                    # Using a card layout for each result
                    with st.container():
                        st.markdown(f"""
                            <div class="card">
                                <div class="card-header">{result.get('name', 'Untitled')}</div>
                                <div class="card-body">
                                    <p>{result.get("description", "No description available.")}</p>
                                    <p><strong>Duration:</strong> {result.get('duration')} minutes</p>
                                    <p><strong>Remote Support:</strong> {result.get('remote_support')}</p>
                                    <p><strong>Adaptive:</strong> {result.get('adaptive')}</p>
                                </div>
                                <div class="card-footer">
                                    <a href="{result.get('url')}" target="_blank" class="button">More Info</a>
                                </div>
                            </div>
                        """, unsafe_allow_html=True)
            else:
                st.warning("No results found.")
        else:
            st.error("Something went wrong fetching data.")
