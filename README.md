# Nabd-AI: Medical-RAG Smart Hospital System

Nabd-AI is a secure, production-ready **Medical Retrieval-Augmented Generation (RAG)** system tailored for the Egyptian healthcare sector. It translates colloquial Arabic symptoms into precise clinical queries, retrieves evidence-based medical knowledge, and utilizes intelligent AI agents for diagnosis support, appointment booking, and hospital workflow automation. Built with **Clean Architecture** principles, Nabd-AI enforces zero-egress data privacy to secure sensitive patient health information.

---

## 🚀 Key Features

- **Colloquial Arabic Translation**: Translates Egyptian dialect symptom descriptions into formal medical terminology and structured clinical queries.
- **Multimodal Document Ingestion**: Employs **Docling (VLM)**, **EasyOCR**, and **Pillow** to dynamically parse structured JSON/CSV data and unstructured PDF medical reports.
- **Clean Architecture & Decoupled Design**: A completely modular design separating API routes, business controllers, vector database adapters, and LLM providers.
- **Hybrid Storage & Vector Search**: Utilizes **FAISS** vector database with **Sentence Transformers (`all-MiniLM-L6-v2`)** for ultra-fast and semantic context retrieval.
- **Production-Ready FastAPI Server**: Decoupled REST endpoints allowing external frontends (e.g., React, Flutter) to integrate seamlessly.
- **Automated RAG Evaluation**: Incorporates the **RAGAS framework** to continuously measure RAG quality using metrics like *Faithfulness*, *Context Recall*, *Context Precision*, and *Answer Correctness*.

---

## 📂 Project Architecture

```
d:/NABD/
├── Data/                       # Ingested datasets & source documents
├── src/                        # Core application code
│   ├── assets/                 # Static assets and archived files
│   ├── controllers/            # Ingest, process, and chat orchestration logic
│   │   ├── ChatController.py
│   │   ├── DataController.py
│   │   └── ProcessController.py
│   ├── helpers/                # Reusable helper functions
│   ├── models/                 # System model schemas
│   ├── routes/                 # FastAPI router paths (e.g., ChatRoutes.py)
│   └── stores/                 # Data access layer
│       └── vectordb/           # Vector Database adapters & factory
│           └── providers/
├── app.py                      # FastAPI App Entrypoint
├── main.py                     # 6-Phase Pipeline CLI Test Script
├── config.py                   # Centralized Configuration & Environment Manager
├── evaluate_rag.py             # RAGAS Evaluation Script
├── eval_dataset.json           # Ground Truth Evaluation Dataset
├── requirements.txt            # Python Dependencies
└── .env                        # Local Environment Secrets (Excluded from Git)
```

---

## 🛠️ Getting Started

### 1. Prerequisites
- Python `3.10` or higher
- Git

### 2. Installation
Clone this repository (or initialize the project locally) and navigate to the project directory:
```bash
git clone https://github.com/Ahmessharf/Nabd-AI.git
cd Nabd-AI
```

Create a virtual environment and activate it:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

### 3. Environment Variables
Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_groq_api_key_here
HF_TOKEN=your_huggingface_token_here (optional)
```

---

## ⚡ Running the Application

### 🧪 Test the 6-Phase Pipeline (CLI)
To run the end-to-end RAG workflow from ingestion to LLM generation:
```bash
python main.py
```
This runs the system through:
1. **Data Ingestion** (Archiving raw medical logs).
2. **Dynamic Parsing** (JSON, CSV, or PDF).
3. **Intelligent Chunking**.
4. **Vector Embedding & Storage** (via FAISS).
5. **Context-Driven Search & Retrieval**.
6. **LLM Generation** (via Groq/Llama-3.1).

### 🌐 Spin up the FastAPI Server
To launch the REST API server:
```bash
python app.py
```
By default, the server runs on `http://127.0.0.1:8000`. You can test the endpoints (e.g., `/chat` and `/health`) using FastAPI's built-in interactive docs at `http://127.0.0.1:8000/docs`.

---

## 🏆 RAGAS Evaluation Pipeline

To evaluate the precision and safety of the RAG system using Ragas:
```bash
python evaluate_rag.py
```
The script runs evaluation samples against the ground-truth answers defined in `eval_dataset.json` and evaluates the performance using:
1. **Context Recall**: Checks if the retrieved context contains all ground-truth facts.
2. **Faithfulness**: Measures if the generated response is strictly grounded in the retrieved context.
3. **Context Precision**: Determines if the most relevant chunks are ranked higher in vector search.
4. **Answer Correctness**: Assesses semantic and factual alignment between the generated response and the ground truth.

Evaluation results are automatically printed to the terminal and exported to [evaluation_results.csv](file:///d:/NABD/evaluation_results.csv).

---

## 📄 License
This project is licensed under the terms specified in the [licence](file:///d:/NABD/licence) file.
