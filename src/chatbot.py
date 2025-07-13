
import ollama
from src.config import RAG_PROMPT_TEMPLATE,OLLAMA_MODEL

def get_rag_response(prompt, vector_store):
    """
    Retrieves context from the vector store and generates a response using the LLM.
    Pega Analogy: This is the load mechanism of a Data Page.
    """
    # 1. Retrieve relevant context
    retriever = vector_store.as_retriever()
    relevant_docs = retriever.invoke(prompt)
    context = "\n\n".join(doc.page_content for doc in relevant_docs)

    # 2. Augment the prompt
    formatted_prompt = RAG_PROMPT_TEMPLATE.format(context=context, prompt=prompt)

    # 3. Generate a response
    stream = ollama.chat(
        model=OLLAMA_MODEL,
        messages=[{"role": "user", "content": formatted_prompt}],
        stream=True,
    )
    
    # Yield each chunk as it comes in
    for chunk in stream:
        yield chunk["message"]["content"]