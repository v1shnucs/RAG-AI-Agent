import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate

# Load environment variables from .env file
load_dotenv()

# Ensure the GOOGLE_API_KEY is set
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in .env file")

# Define the path for storing the FAISS index
DB_FAISS_PATH = 'vectorstore/db_faiss'

def create_vector_store(documents_path='documents'):
    """
    Loads documents, splits them into chunks, creates embeddings,
    and stores them in a FAISS vector store.
    """
    print("Loading documents...")
    # For now, we'll just handle PDFs. This can be extended.
    all_docs = []
    for filename in os.listdir(documents_path):
        if filename.endswith('.pdf'):
            loader = PyPDFLoader(os.path.join(documents_path, filename))
            all_docs.extend(loader.load())

    if not all_docs:
        print("No PDF documents found in the documents directory.")
        return

    print("Splitting documents into chunks...")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    text_chunks = text_splitter.split_documents(all_docs)

    print("Creating embeddings...")
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    print("Creating and saving FAISS vector store...")
    db = FAISS.from_documents(text_chunks, embeddings)
    db.save_local(DB_FAISS_PATH)
    print("Vector store created and saved.")

# This is a placeholder for the conversational chain, which we will build out next.
def get_conversational_chain():
    """
    Creates and returns a conversational QA chain.
    """
    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
    provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """

    model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=api_key, temperature=0.3)
    
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    
    return chain

if __name__ == '__main__':
    # This allows us to run this script directly to create the vector store
    # Make sure you have some PDF files in the 'documents' directory before running.
    if not os.path.exists('documents') or not os.listdir('documents'):
        print("The 'documents' directory is empty or does not exist.")
        print("Please add some PDF files to the 'documents' directory and run this script again.")
    else:
        create_vector_store()