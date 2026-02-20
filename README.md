TripGenie – Custom RAG-Based Travel Assistant (FAISS + Groq + ScaleDown)
An AI-powered Travel Planning Assistant built using a custom Retrieval-Augmented Generation (RAG) pipeline.
TripGenie generates intelligent, structured travel itineraries using semantic search over a self-built travel dataset and LLM generation via Groq API.
🚀 Project Overview
TripGenie is a fully custom RAG system developed without heavy frameworks, using FAISS vector search, SentenceTransformers embeddings, and external APIs for LLM generation and context compression.
Unlike generic chatbot systems, this project:
Uses a self-built FAISS vector database (travel_index.faiss)
Retrieves real contextual chunks from scraped travel data
Compresses context using ScaleDown API
Generates final itineraries using Groq LLM (Llama 3.1)
🧠 Complete Architecture Flow
User Query
→ SentenceTransformer Embedding (all-MiniLM-L6-v2)
→ FAISS Semantic Search (travel_index.faiss)
→ Top-K Chunk Retrieval (chunks.pkl)
→ Context Compression (ScaleDown API)
→ LLM Generation (Groq API – Llama 3.1 8B Instant)
→ JSON Travel Itinerary + Image Enrichment
✨ Core Features (Actual Implementation)
Custom RAG Pipeline (No LangChain dependency)
FAISS Vector Database (Locally Built Index)
Semantic Search over Travel Dataset (.txt files)
Dynamic Itinerary Generation (Days + Budget aware)
Context Compression using ScaleDown API
LLM Response Generation via Groq API
Image enrichment using Pixel/Unsplash-style API
Flask REST API Backend
Clean structured JSON output for frontend integration
Custom Scraper + Chunking System
🛠️ Actual Tech Stack (Project Accurate)
🖥 Backend
Python 3.12
Flask
Flask-CORS
Python-dotenv
Requests
🤖 AI / RAG Components
SentenceTransformers (all-MiniLM-L6-v2)
FAISS (CPU) – Vector Search Engine
NumPy – Embedding Handling
Custom Chunking Logic (chunker.py, chunks.pkl)
🔌 External APIs (ONLY These Used)
Groq API → LLM Generation (Llama 3.1 8B Instant)
ScaleDown API → Context Compression
Pixel / Unsplash Image API → Destination Images
📁 Real Project Structure (Based on Your Backend Folder)
Bash
Copy code
TripGenie/
└── backend/
    ├── app.py                # Main Flask RAG server
    ├── build_index.py        # Builds FAISS vector index
    ├── scraper.py            # Travel data scraping script
    ├── chunker.py            # Chunk processing logic
    ├── chunks.py             # Chunk loader (pickle based)
    ├── fias.py               # FAISS utility logic
    ├── data/                 # Travel text dataset (.txt files)
    ├── travel_index.faiss    # Generated FAISS index (vector DB)
    ├── chunks.pkl            # Stored chunks + metadata
    ├── .env                  # API keys (ignored in Git)
    ├── requirements.txt
    ├── runtime.txt
    └── venv/                 # Virtual environment (ignored)
🔑 Environment Variables (IMPORTANT)
Create a .env file inside the backend folder:
Env
Copy code
GROQ_API_KEY=your_groq_api_key
SCALEDOWN_API_KEY=your_scaledown_api_key
PIXEL_API_KEY=your_image_api_key
⚠️ Do NOT push .env to GitHub.
⚙️ Installation Guide (Step-by-Step)
1️⃣ Clone the Repository
Bash
Copy code
git clone https://github.com/yourusername/tripgenie.git
cd TripGenie/backend
2️⃣ Create Virtual Environment
Bash
Copy code
python -m venv venv
Activate (Windows PowerShell):
Bash
Copy code
venv\Scripts\activate
3️⃣ Install Dependencies
Bash
Copy code
pip install -r requirements.txt
OR manual:
Bash
Copy code
pip install flask flask-cors faiss-cpu numpy requests sentence-transformers python-dotenv
🧱 Building the FAISS Index (MANDATORY)
Since the project uses a custom dataset, you must generate the vector database:
Bash
Copy code
python build_index.py
This will automatically create:
travel_index.faiss → Vector index
chunks.pkl → Stored text chunks + metadata
Console Output Example:
Copy code

FAISS index built with 50 vectors
Done! Both FAISS and pickle rebuilt successfully.
▶️ Running the Backend Server
Make sure you are inside:
Copy code

TripGenie/backend
Then run:
Bash
Copy code
python app.py