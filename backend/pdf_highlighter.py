import fitz  
from rapidfuzz import fuzz
import re
from langchain.schema import Document
from typing import List


def highlight_chunks_in_pdf(documents: List[Document], output_path: str = None):
    """
    Highlight chunks in PDF and save to specified output path
    """
    if not documents:
        print("No documents provided. Aborting.")
        return False
    
    pdf_path = documents[0].metadata.get("source")
    if not pdf_path:
        print("No 'source' in metadata. Aborting.")
        return False
    
    # Use provided output path or generate one
    if output_path is None:
        pdf_file = Path(pdf_path)
        output_path = pdf_file.stem + "_highlighted" + pdf_file.suffix
    
    try:
        doc = fitz.open(pdf_path)
        
        for document in documents:
            page_number = document.metadata.get("page", 0)
            text_to_highlight = document.page_content
            
            if page_number < 0 or page_number >= len(doc):
                print(f"Page {page_number} doesn't exist in PDF. Skipping this chunk.")
                continue
            
            page = doc[page_number]
            # Normalize text for better matching
            normalized_text = " ".join(text_to_highlight.split())
            matches = page.search_for(normalized_text)
            
            for match in matches:
                page.add_highlight_annot(match)
        
        doc.save(output_path)
        doc.close()
        print(f"Highlights saved to '{output_path}'")
        return True
        
    except Exception as e:
        print(f"Error highlighting PDF: {e}")
        return False
