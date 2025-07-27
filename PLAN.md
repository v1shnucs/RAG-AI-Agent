# Project Plan: RAG-Powered Web Application with Gemini

This document outlines the detailed plan for building a Retrieval-Augmented Generation (RAG) web application. The backend will be built with Python (FastAPI) and the RAG pipeline will use Google's Gemini model, FAISS for vector storage, and LangChain. The frontend will be a Next.js application.

---

## Phase 1: Project Setup & Core Backend

**Objective:** Establish the project structure, set up the Python environment, and create a basic, running FastAPI application.

- **Task 1.1: Create Project Directories**
  - Create a root directory for the project.
  - Inside the root, create the following structure:
    ```
    /
    ├── backend/
    │   └── app/
    │       ├── api/
    │       └── core/
    ├── documents/
    └── frontend/
    ```

- **Task 1.2: Set Up Python Virtual Environment**
  - Navigate into the `backend` directory.
  - Create a Python virtual environment: `python -m venv venv`
  - Activate the environment: `source venv/bin/activate` (macOS/Linux) or `venv\Scripts\activate` (Windows).

- **Task 1.3: Install Initial Python Dependencies**
  - With the virtual environment activated, install the necessary libraries:
    ```bash
    pip install fastapi uvicorn python-dotenv google-generativeai langchain langchain-google-genai faiss-cpu pypdf sentence-transformers
    ```

- **Task 1.4: Configure Environment Variables**
  - In the `backend` directory, create a `.env` file.
  - Add your Google API key to this file:
    ```
    GOOGLE_API_KEY="YOUR_API_KEY_HERE"
    ```

- **Task 1.5: Create Basic FastAPI App**
  - In `backend/app/main.py`, create a minimal FastAPI application with a health check endpoint to confirm it's running.
    ```python
    from fastapi import FastAPI

    app = FastAPI()

    @app.get("/")
    def read_root():
        return {"status": "ok"}
    ```

---

## Phase 2: RAG Pipeline Implementation (Backend)

**Objective:** Build the core RAG logic that can load documents, create a vector store, and answer questions using the Gemini model.

- **Task 2.1: Implement Document Loading**
  - In a new file, `backend/app/core/rag.py`, use `PyPDFLoader` from LangChain to load PDF documents from the `/documents` directory.

- **Task 2.2: Implement Text Splitting**
  - In the same file, use `RecursiveCharacterTextSplitter` to break the loaded documents into smaller, semantically meaningful chunks.

- **Task 2.3: Implement Embedding Logic**
  - Use `HuggingFaceEmbeddings` with a model like `all-MiniLM-L6-v2` to convert the text chunks into vector embeddings.

- **Task 2.4: Build and Save FAISS Vector Store**
  - Create a function that takes the embedded chunks and builds a FAISS index.
  - Save the FAISS index to disk so it can be loaded quickly without re-indexing every time.

- **Task 2.5: Implement the QA Chain**
  - Use `ChatGoogleGenerativeAI` to initialize the Gemini model.
  - Create a `RetrievalQA` chain from LangChain, combining the LLM with the FAISS retriever.

- **Task 2.6: Create the API Endpoint**
  - In `backend/app/api/endpoints.py`, create an `/api/ask` endpoint.
  - This endpoint will take a user's question, pass it to the RAG chain, and return the generated answer.

---

## Phase 3: Frontend Setup (Next.js)

**Objective:** Create a user-facing interface to interact with the backend.

- **Task 3.1: Initialize Next.js Project**
  - Navigate to the `frontend` directory.
  - Run `npx create-next-app@latest .` to create a new Next.js application.

- **Task 3.2: Build the Chat Interface**
  - Create a simple, clean chat component.
  - This component should include a message history display and a text input field with a "Send" button.

- **Task 3.3: Connect Frontend to Backend**
  - Implement the client-side logic to make an API call to the backend's `/api/ask` endpoint when the user sends a message.
  - Display the response from the backend in the chat history.

---

## Phase 4: Finalizing and Connecting

**Objective:** Add key features like file uploads and source citations, and ensure seamless communication between the frontend and backend.

- **Task 4.1: Configure CORS**
  - In the FastAPI app (`backend/app/main.py`), add CORS middleware to allow requests from your frontend's domain.

- **Task 4.2: Implement File Upload**
  - **Frontend:** Add a file upload button to the UI.
  - **Backend:** Create an `/api/upload` endpoint that accepts a file, saves it to the `/documents` directory, and triggers a re-indexing of the FAISS vector store.

- **Task 4.3: Return Source Documents**
  - Modify the `RetrievalQA` chain to return the source documents (the specific chunks) that were used to generate the answer.

- **Task 4.4: Display Sources in UI**
  - In the frontend, display the source information alongside the answer, allowing users to see where the information came from.

---

## Phase 5: Containerization & Documentation

**Objective:** Make the project easy to set up, run, and deploy using Docker, and provide clear documentation.

- **Task 5.1: Write a Backend Dockerfile**
  - Create a `Dockerfile` in the `backend` directory to containerize the FastAPI application.

- **Task 5.2: Create a Docker Compose File**
  - In the root directory, create a `docker-compose.yml` file.
  - This file will define the services for both the backend and frontend, making it possible to launch the entire application with a single command (`docker-compose up`).

- **Task 5.3: Write Comprehensive Documentation**
  - In the root directory, create a `README.md` file.
  - The README should include:
    - A project overview.
    - Architecture diagram.
    - Instructions for setting up and running the project (both locally and with Docker).
    - API endpoint documentation.