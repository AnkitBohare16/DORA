import streamlit as st
from dotenv import load_dotenv
# import time
from src.helper import get_pdf_text, get_text_chunks, get_vector_store, get_conversational_chain


def user_input(user_quesiton):
        response = st.session_state.conversation({"question": user_quesiton})
        st.session_state.chat_history = response["chat_history"]
        for i, message in enumerate(st.session_state.chat_history):
            if i % 2 == 0:
                st.markdown(f"**User:** {message.content}")
            else:
                st.markdown(f"**Reply:** {message.content}")


def main():
    load_dotenv()
    st.set_page_config("DORA")
    st.header("Information Retrieval System")
    
    user_quesiton = st.text_input("Ask a question about your documents here:")
    
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    if user_quesiton:
        user_input(user_quesiton)
        
            
            
    
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