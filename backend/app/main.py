from fastapi import FastAPI
from app.api.endpoints import router as api_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="RAG-powered API with Gemini and FAISS")

# Set up CORS to allow requests from the frontend
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:3001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the API router
app.include_router(api_router, prefix="/api")

@app.get("/", tags=["Health Check"])
def read_root():
    """A simple health check endpoint to confirm the API is running."""
    return {"status": "ok", "message": "API is running"}