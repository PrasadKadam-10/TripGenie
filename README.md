✈️ TripGenie – Custom RAG-Based Travel Assistant

<p align="center">
  <img src="https://img.shields.io/badge/STATUS-PRODUCTION_READY-brightgreen?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/ARCHITECTURE-CUSTOM_RAG-blueviolet?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/BACKEND-FLASK_API-orange?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/LLM-GROQ_LLAMA3.1-red?style=for-the-badge"/>
</p>---

<h2 align="center">🌍 AI-Powered Intelligent Travel Itinerary Generator</h2><p align="center">
A fully custom Retrieval-Augmented Generation (RAG) Travel Assistant that generates structured, context-aware travel itineraries using semantic search, compressed knowledge retrieval, and LLM-based generation.
</p>---

🧠 Project Overview

TripGenie is an advanced AI travel planning assistant built with a custom RAG pipeline instead of heavy frameworks like LangChain.
It retrieves real contextual travel data from a self-built vector database, compresses it efficiently, and generates intelligent itineraries using a high-speed LLM.

Unlike basic recommendation systems, this project:

- Uses a local FAISS vector database (not generic APIs)
- Retrieves semantic travel knowledge chunks
- Compresses context using ScaleDown API
- Generates detailed itineraries using Groq LLM
- Enriches results with destination images via Pixel API

---

🚀 Core Features (Actual Implementation)

- 🔎 Semantic Search using FAISS Vector Database
- 🧩 Custom Chunking & Retrieval System
- 🧠 Retrieval-Augmented Generation (RAG) Pipeline
- ⚡ Ultra-fast LLM generation via Groq (Llama 3.1)
- 🗜️ Context Compression using ScaleDown API
- 🖼️ Dynamic Image Enrichment using Pixel API
- 📊 Structured JSON Travel Itinerary Output
- 🌐 REST API Backend (Flask + CORS)
- 📁 Self-built Travel Dataset (.txt based)
- 🧪 Fully Custom Backend (No LangChain dependency)

---
``` 



User Query
   ↓
SentenceTransformer Embedding
   ↓
FAISS Semantic Search
   ↓
Top-K Chunk Retrieval
   ↓
Context Compression (ScaleDown)
   ↓
LLM Generation (Groq)
   ↓
Structured JSON + Destination Images

``` 



---

🛠️ Actual Tech Stack (Project Accurate)

<h3 align="center">🖥️ Backend Technologies</h3><p align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="50"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg" height="50"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg" height="50"/>
</p>- Python 3.12
- Flask (REST API Server)
- Flask-CORS
- Requests
- Python-dotenv

---
"``` 
<h3 align="center">🤖 AI / RAG Components</h3>- SentenceTransformers (all-MiniLM-L6-v2) – Embeddings
- FAISS (CPU) – Vector Search Engine
- NumPy – Embedding Processing
- Custom Chunking Logic (chunker.py)
- Pickle-based Chunk Storage (chunks.pkl)

``` "

---
``` 

<h3 align="center">🔌 External APIs (ONLY APIs USED)</h3>API| Purpose
Groq API| LLM Itinerary Generation (Llama 3.1 8B Instant)
ScaleDown API| Context Compression
Pixel / Image API| Destination Image Fetching
"
``` 
---

📁 Real Project Structure (Based on Your Backend)
```
TripGenie/
├─ backend/
│   ├─ app.py
│   ├─ build_index.py
│   ├─ scraper.py
│   ├─ chunker.py
│   ├─ chunks.py
│   ├─ fias.py
│   ├─ data/
│   ├─ travel_index.faiss
│   ├─ chunks.pkl
│   ├─ requirements.txt
│   ├─ runtime.txt
│   └─ .env
└─ frontend/ 
---
``` 

Create a ".env" file inside the backend folder:

GROQ_API_KEY=your_groq_api_key
SCALEDOWN_API_KEY=your_scaledown_api_key
PIXEL_API_KEY=your_pixel_api_key

⚠️ Never push ".env" file to GitHub for security reasons.

---

⚙️ Installation Guide (Step-by-Step)

1️⃣ Clone the Repository

git clone https://github.com/yourusername/TripGenie.git
cd TripGenie/backend

2️⃣ Create Virtual Environment

python -m venv venv

Activate (Windows):

venv\Scripts\activate

3️⃣ Install Dependencies

pip install -r requirements.txt

Or manual install:

pip install flask flask-cors faiss-cpu numpy requests sentence-transformers python-dotenv

---

🧱 Building the FAISS Vector Index (Mandatory Step)

Since the system uses a custom dataset, you must generate the vector database before running the server.

Run:

python build_index.py

This will automatically generate:

- "travel_index.faiss" → Vector Search Index
- "chunks.pkl" → Chunked dataset + metadata

Example Output:

FAISS index built successfully with travel dataset vectors
Chunks stored in chunks.pkl

---

▶️ Running the Backend Server

Navigate to:

TripGenie/backend

Then start the Flask server:

python app.py

Server will run on:

http://127.0.0.1:5000

---

🌐 API Endpoint (Core RAG Endpoint)

Method| Endpoint| Description
POST| /generate-itinerary| Generates AI travel plan using RAG

Input:

{
  "destination": "Goa",
  "days": 3,
  "budget": "medium"
}

Output:

- Structured JSON itinerary
- Day-wise planning
- Image enriched response

---

🎯 Key Innovations in This Project

- Custom RAG pipeline without LangChain
- Self-built FAISS vector database
- Context compression before LLM (cost optimized)
- Lightweight yet scalable architecture
- Real dataset-driven travel recommendations
- API-first modular backend design

---

🔮 Future Improvements

- Frontend React Integration
- User personalization memory
- Budget-based smart filtering
- Multi-destination itinerary planning
- Cloud deployment (Render / AWS)
- Larger semantic travel dataset

---

👨‍💻 Author

Prasad Dilip Kadam
B.Tech IT Engineer | AI & RAG System Developer
Frontend Developer – Cyber Arena Project
Passionate about AI Systems, RAG Pipelines & Web Technology

---

<p align="center">
⭐ If you find this project innovative, consider starring the repository!
</p>
