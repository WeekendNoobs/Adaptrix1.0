import streamlit as st

st.set_page_config(page_title="My RAG Chatbot",page_icon=':material/robot_2:' ,layout="wide")

#Title
st.title("🤖 Upload and Chat with your Docs")
st.caption("This is a sample app for the RAG tutorials")

#Sidebar
with st.sidebar :
    st.header("Controls")
    uploaded_docs = st.file_uploader("Upload your Documents",type="pdf")

# Start the state management
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role":"assistant","content":"Hello!I am a simple chatbot.How can I help you?"}
    ]

#Chat inputbox
if prompt:= st.chat_input("Ask any question ..."):
    st.session_state.messages.append({"role":"user","content":prompt})

#Assistanc Response Dummy
if prompt:
    assistance_reponse = f"Echo: I will answer your question :- {prompt}"
    st.session_state.messages.append({"role":"assistant","content":assistance_reponse})

# debugging purpose only 
# st.write(st.session_state)

for message in st.session_state.messages :
    with st.chat_message(message["role"]):
        st.markdown(message["content"])




