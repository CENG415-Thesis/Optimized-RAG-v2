from langchain_ollama import OllamaEmbeddings

def get_embedding_function():
    
    embeddings = OllamaEmbeddings(model="nomic-embed-text") 
    #Try another embeddings, HuggingFace Embeddings                                
    
    return embeddings