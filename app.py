import streamlit as st
from query_data import query_rag

st.title("RAG Pipeline Query Interface")

query_text = st.text_area("Enter your query about the PDF:", height=100)

if st.button("Submit"):
    if query_text:
        with st.spinner("Processing..."):
            response_text = query_rag(query_text)
            st.success("Query processed successfully!")
            st.write("### Response:")
            st.write(response_text)
    else:
        st.error("Please enter a query.")