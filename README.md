✈️ TripGenie – AI Travel Assistant








🌍 What is TripGenie?

TripGenie is an AI-powered travel itinerary generator built with a custom RAG pipeline.
It retrieves real travel knowledge from a self-built FAISS vector database, compresses context, and generates structured, image-enriched itineraries.

Why it’s different:

Custom FAISS-based semantic search

No heavy frameworks like LangChain

Context compression via ScaleDown API

LLM-powered itinerary generation (Groq Llama 3.1)

Destination images via Pixel API

🚀 Core Features
Feature	Description
🔎 Semantic Search	FAISS vector database retrieval
🧩 Chunking	Custom chunking logic for text
🧠 RAG Pipeline	Context + LLM-based itinerary
⚡ LLM Generation	Groq Llama 3.1 (fast & smart)
🗜️ Context Compression	ScaleDown API
🖼️ Image Enrichment	Pixel API for destination images
📊 Output	Structured JSON itineraries
🌐 Backend	REST API (Flask + CORS)
🏗️ How It Works
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
🛠️ Tech Stack

Backend: Python 3.12 + Flask + NumPy
AI / RAG: SentenceTransformers, FAISS, custom chunking, pickle storage
External APIs: Groq, ScaleDown, Pixel

📁 Project Structure
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
└─ frontend/ (optional)
⚙️ Installation & Run

1️⃣ Clone & navigate:

git clone https://github.com/yourusername/TripGenie.git
cd TripGenie/backend

2️⃣ Setup virtual environment:

python -m venv venv
# Windows
venv\Scripts\activate

3️⃣ Install dependencies:

pip install -r requirements.txt

4️⃣ Build FAISS index:

python build_index.py

5️⃣ Run server:

python app.py

Access at: http://127.0.0.1:5000

API Endpoint: POST /generate-itinerary

{
  "destination": "Goa",
  "days": 3,
  "budget": "medium"
}
🔮 Future Plans

React frontend integration

User personalization

Multi-destination itinerary planning

Cloud deployment (Render / AWS)

Expanded travel dataset

👨‍💻 Author

Prasad Dilip Kadam – B.Tech IT | AI & RAG Developer | Frontend Developer – Cyber Arena Project

⭐ Star the repo if you find it useful!
