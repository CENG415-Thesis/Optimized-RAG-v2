import streamlit as st
from query_data import query_rag

st.title("RAG Pipeline Query Interface")

# Initialize session state for query history
if 'history' not in st.session_state:
    st.session_state.history = []

query_text = st.text_area("Enter your query about the PDF:", height=100)

# Custom CSS for the button
st.markdown("""
    <style>
    .chatgpt-button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 12px;
        border: none;
    }
    .chatgpt-button:hover {
        background-color: #45a049;
    }
    .chat-bubble {
        background-color: #f1f1f1;
        border-radius: 10px;
        padding: 10px;
        margin: 10px 0;
        width: fit-content;
        max-width: 80%;
        color: black;
    }
    .chat-bubble.user {
        background-color: #DCF8C6;
        align-self: flex-end;
    }
    .chat-bubble.bot {
        background-color: #ECECEC;
        align-self: flex-start;
    }
    .chat-container {
        display: flex;
        flex-direction: column;
    }
    </style>
""", unsafe_allow_html=True)

# Custom button with icon
if st.button('Submit ➤', key='submit_button'):
    if query_text:
        with st.spinner("Processing..."):
            response_text = query_rag(query_text)
            st.session_state.history.append({"query": query_text, "response": response_text})
            st.success("Query processed successfully!")
    else:
        st.error("Please enter a query.")

# Display chat history
st.write("### Chat History")
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for entry in st.session_state.history:
    st.markdown(f'<div class="chat-bubble user"><strong>You:</strong> {entry["query"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="chat-bubble bot"><strong>Bot:</strong> {entry["response"]}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)