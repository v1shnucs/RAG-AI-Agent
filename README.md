# RAG-powered Chat Application

This project is a web-based chat application that uses a Retrieval-Augmented Generation (RAG) pipeline to answer questions based on a set of documents. The backend is built with FastAPI and the frontend is built with Next.js.

## Features

- **Chat Interface:** A simple, intuitive chat interface to interact with the RAG model.
- **Document Upload:** Upload your own PDF documents to be used as the knowledge base.
- **Source Citations:** The model provides citations for its answers, so you can verify the information.

## Tech Stack

- **Backend:** FastAPI, LangChain, Gemini, FAISS
- **Frontend:** Next.js, React, Tailwind CSS

## Getting Started

### Prerequisites

- Python 3.9 or higher
- Node.js and npm
- A Google API key with the Gemini API enabled

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/v1shnucs/RAG-AI-Agent.git
   cd RAG-AI-Agent
   ```

2. **Set up the backend:**
   - Navigate to the `backend` directory:
     ```bash
     cd backend
     ```
   - Create a virtual environment:
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
     ```
   - Install the required Python packages:
     ```bash
     pip install -r requirements.txt
     ```
   - Create a `.env` file in the `backend` directory and add your Google API key:
     ```
     GOOGLE_API_KEY="your-google-api-key"
     ```

3. **Add your documents:**
   - Place your PDF documents in the `documents` directory.

4. **Create the vector store:**
   - While in the backend virtual environment, run:
     ```bash
     python app/core/rag.py
     ```

5. **Start the backend server:**
   ```bash
   uvicorn app.main:app --reload
   ```
   The backend will be available at `http://localhost:8000`.

6. **Set up the frontend:**
   - In a new terminal, navigate to the `frontend` directory:
     ```bash
     cd frontend
     ```
   - Install the required Node.js packages:
     ```bash
     npm install
     ```

7. **Start the frontend server:**
   ```bash
   npm run dev
   ```
   The frontend will be available at `http://localhost:3000` (or another port if 3000 is in use).

### Usage

1. **Open the application:**
   - Open your web browser and navigate to `http://localhost:3000` (or the port shown in the terminal).

2. **Ask a question:**
   - Type a question in the input field and press Enter or click the "Send" button.

3. **Upload a document:**
   - Click the "Upload PDF" button to upload a new document. The vector store will be automatically updated.

## Project Structure

```
.
├── backend
│   ├── app
│   │   ├── api
│   │   │   └── endpoints.py
│   │   ├── core
│   │   │   └── rag.py
│   │   └── main.py
│   ├── documents
│   │   └── ...
│   ├── venv
│   │   └── ...
│   ├── requirements.txt
│   └── .env
├── frontend
│   ├── src
│   │   ├── app
│   │   │   ├── components
│   │   │   │   └── Chat.tsx
│   │   │   └── page.tsx
│   │   └── ...
│   ├── package.json
│   └── ...
└── README.md