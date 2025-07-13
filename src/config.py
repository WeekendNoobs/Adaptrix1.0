
# Model and Embedding Configuration
OLLAMA_MODEL = "gemma:2b"
EMBEDDING_MODEL = "gemma:2b"

# Text Splitter Configuration
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 100

# RAG Prompt Template
RAG_PROMPT_TEMPLATE = """You are a helpful assistant. 
Your task is to answer the user's question based ONLY on the context provided below.
If the context does not contain the answer, you MUST say "I cannot find the answer in the document." 
Do not use any of your outside knowledge.

CONTEXT:
{context}

QUESTION:
{prompt}
"""