import streamlit as st
# from dotenv import load_dotenv
# import time
from src.helper import get_pdf_text, get_text_chunks, get_vector_store, get_conversational_chain

def main():
    load_dotenv()
    st.set_page_config("DORA")
    st.header("Information Retrieval System")
    
    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF files here and click on 'Submit & Process'", accept_multiple_files=True)
        
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                # time.sleep(2)  
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                vectorstore = get_vector_store(text_chunks)
                st.session_state.conversation = get_conversational_chain(vectorstore)
            
                st.success("Done")
     
      
    

if __name__ == "__main__":
    main()