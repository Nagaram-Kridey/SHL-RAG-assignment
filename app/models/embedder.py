import os
import cohere
from dotenv import load_dotenv  # 👈 Add this line

load_dotenv()

co = cohere.Client(os.getenv("COHERE_API_KEY"))

def get_embedding(text):
    response = co.embed(
        texts=[text],
        model="embed-english-v3.0",
        input_type="search_query"
    )
    return response.embeddings[0]
