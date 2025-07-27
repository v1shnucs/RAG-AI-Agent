# RAG-powered Chat Application

This project is a web-based chat application that uses a Retrieval-Augmented Generation (RAG) pipeline to answer questions based on a set of documents. The backend is built with FastAPI and the frontend is built with Next.js.

## Features

- **Chat Interface:** A simple, intuitive chat interface to interact with the RAG model.
- **Document Upload:** Upload your own PDF documents to be used as the knowledge base.
- **Source Citations:** The model provides citations for its answers, so you can verify the information.
- **Containerized:** The entire application can be run with Docker Compose, making it easy to set up and run.

## Tech Stack

- **Backend:** FastAPI, LangChain, Gemini, FAISS
- **Frontend:** Next.js, React, Tailwind CSS
- **Containerization:** Docker, Docker Compose

## Getting Started

### Prerequisites

- Docker and Docker Compose
- A Google API key with the Gemini API enabled

### Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. **Create a `.env` file:**
   - In the `backend` directory, create a file named `.env`.
   - Add your Google API key to the file:
     ```
     GOOGLE_API_KEY="your-google-api-key"
     ```

3. **Add your documents:**
   - Place your PDF documents in the `documents` directory.

4. **Build and run the application:**
   ```bash
   docker-compose up --build
   ```

### Usage

1. **Open the application:**
   - Open your web browser and navigate to `http://localhost:3000`.

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
│   ├── Dockerfile
│   └── requirements.txt
├── documents
│   └── ...
├── frontend
│   ├── src
│   │   ├── app
│   │   │   ├── components
│   │   │   │   └── Chat.tsx
│   │   │   └── page.tsx
│   └── Dockerfile
├── docker-compose.yml
└── README.md