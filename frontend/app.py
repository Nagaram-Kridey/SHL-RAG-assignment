import streamlit as st
import requests
import subprocess

st.title("SHL Assessment Recommender")

if st.button("🔄 Run Web Scraper (dataloader.py)"):
    with st.spinner("Scraping data from SHL..."):
        result = subprocess.run(["python", "app/dataloader.py"], capture_output=True, text=True)
        if result.returncode == 0:
            st.success("✅ Data loaded successfully!")
        else:
            st.error("❌ Scraping failed!")
            st.text(result.stderr)

query = st.text_area("Enter job description or requirement:")
if st.button("Get Recommendations"):
    res = requests.post("http://localhost:8000/recommend", json={"query": query})
    for r in res.json()["results"]:
        st.markdown(f"**[{r['name']}]({r['url']})** - {r['type']}")
        st.write(f"🕒 {r['duration']} | Remote: {r['remote_support']} | Adaptive: {r['adaptive']}")
        st.markdown("---")
