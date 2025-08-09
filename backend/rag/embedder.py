from langchain_google_genai import GoogleGenerativeAIEmbeddings

def get_embedder():
    return GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
