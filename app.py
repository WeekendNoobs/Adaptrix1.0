# app.py

import streamlit as st
from src.rag_logic import process_document
from src.chatbot import get_rag_response

# --- UI Configuration ---
st.set_page_config(page_title="Enterprise RAG Chatbot", layout="wide")

# Helper function for CSS (can be moved to a utils.py in a larger app)
def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("assets/global.css")

# --- UI Sections ---
st.title("🤖 Upload and Chat with your Docs")
st.caption("An enterprise-structured RAG application")

with st.sidebar:
    st.header("Controls")
    uploaded_file = st.file_uploader("Upload your Documents", type="pdf")
    process_button = st.button("Process Document")

# --- Session State Management (The "Clipboard") ---
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hello! Please upload a document to begin."}]
if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

# --- Main Application Flow ---

# Display existing chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle document processing on button click
if process_button and uploaded_file:
    with st.spinner("Processing Document..."):
        vector_store = process_document(uploaded_file)
        if vector_store:
            st.session_state.vector_store = vector_store
            st.session_state.messages = [{"role": "assistant", "content": "Knowledge base ready. Ask me anything about your document!"}]
            st.rerun()

# Handle user chat input
if prompt := st.chat_input("Ask a question about your document..."):
    # Display user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate and display assistant response
    if st.session_state.vector_store:
        with st.chat_message("assistant"):
            response_stream = get_rag_response(prompt, st.session_state.vector_store)
            full_response = st.write_stream(response_stream)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
    else:
        with st.chat_message("assistant"):
            st.warning("Please upload and process a document first.")