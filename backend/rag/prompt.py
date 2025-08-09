from langchain.prompts import ChatPromptTemplate

def get_prompt():
    return ChatPromptTemplate.from_template("""
Use the context below to answer the question using only the information found in the context.

Respond with a short phrase, one or two words, or a single sentence at most.  
Do not explain or generalize. Keep your answer brief and factual.

---

Now answer the following:

Context:
{context}

Question:
{question}

Answer:
""")
