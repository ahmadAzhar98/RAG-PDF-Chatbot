# frontend/app.py
import streamlit as st
import requests
import tempfile
import os
import base64

st.set_page_config(page_title="PDF QA with Highlighting", layout="wide")
st.title("📘 PDF Q&A with Context Highlighting")

uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])
question = st.text_input("Enter your question:")

if uploaded_file:
    # Save uploaded PDF to temp path
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name
    
    # Render PDF preview
    with st.expander("📄 Preview PDF"):
        with open(tmp_path, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode("utf-8")
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800" type="application/pdf"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)
    
    if question:
        with st.spinner("Thinking..."):
            response = requests.post(
                "http://localhost:8000/ask",
                json={"question": question, "pdf_path": tmp_path, "highlight": True}
            )
            
            if response.status_code == 200:
                data = response.json()
                st.subheader("📄 Answer")
                st.write(data["answer"])
                
                # Show highlighted PDF instead of text chunks
                if data.get("highlighted_pdf"):
                    st.subheader(" 📑 Highlighted PDF")
                    with open(data["highlighted_pdf"], "rb") as f:
                        base64_pdf = base64.b64encode(f.read()).decode("utf-8")
                        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800" type="application/pdf"></iframe>'
                        st.markdown(pdf_display, unsafe_allow_html=True)
                else:
                    st.error("Could not highlight chunks in PDF")
            else:
                st.error("Backend error. Please check FastAPI logs.")
else:
    st.info("Please upload a PDF file.")