
import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter as RCTSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from src.config import CHUNK_SIZE, CHUNK_OVERLAP, EMBEDDING_MODEL

def process_document(uploaded_file):
    """
    Loads a PDF, splits it into chunks, creates embeddings, and returns a vector store.
    Pega Analogy: This is the main processing Activity called by a Service-File rule.
    """
    try:
        # Save the uploaded file to a temporary path
        temp_file_path = "temp.pdf"
        with open(temp_file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # 1. Load the document
        loader = PyPDFLoader(temp_file_path)
        documents = loader.load()

        # 2. Split the document into chunks
        text_splitter = RCTSplitter(
            chunk_size=CHUNK_SIZE, 
            chunk_overlap=CHUNK_OVERLAP
        )
        chunks = text_splitter.split_documents(documents)

        # 3. Create embeddings
        embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL)

        # 4. Create the vector store
        vector_store = FAISS.from_documents(chunks, embeddings)
        return vector_store

    except Exception as e:
        st.error(f"Error processing document: {e}")
        return None
