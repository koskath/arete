# ARETE

<div align="center">
  <img src="arete_deployment/app/icon.svg" alt="ARETE Logo" width="200" height="200">
  
  **AI Research Ecosystem for Teaching Experiment**
  
  *An intelligent educational chatbot system for Copenhagen Business School*
</div>

---

## About ARETE

ARETE (AI Research Ecosystem for Teaching Experiment) is an educational chatbot platform designed to support students at Copenhagen Business School. The system leverages Fine tuned open source Small Language Models with Retrieval Augmented Generation (RAG) technology to provide step to step guidance and course-specific assistance across multiple disciplines.

ARETE serves as a friendly and supportive teaching assistant that helps students with:
- **Machine Learning** concepts and problem-solving
- **Supply Chain Management** principles and applications  
- **Internet of Things** development and troubleshooting

---

## Contact

For questions, feedback, or collaboration opportunities, please reach out:

- **Email:** kok.digi@cbs.dk
- **GitHub:** [koskath/arete](https://github.com/koskath/arete)
- **LinkedIn:** [Konstantinos Katharakis](www.linkedin.com/in/konstantinos-katharakis)
- **Institution:** [Copenhagen Business School - Department of Digitalisation](https://www.cbs.dk/en/research/departments/department-digitalisation)

---

## Project Structure

This repository contains two main components:

### 📦 `arete_deployment`

The deployment folder contains the production-ready application consisting of:

- **Backend API** (`app.py`): FastAPI-based REST API that handles chat requests, streaming responses, and conversation management
- **Frontend Application** (`app/`): Next.js React application with TypeScript providing an intuitive chat interface
- **RAG Pipeline** (`rag_pipeline.py`): Retrieval Augmented Generation system that searches vector stores for relevant course content
- **Model Integration** (`instruct_model.py`): Interfaces with various LLM providers (HuggingFace, Llama Cloud, Codestral) for generating responses
- **Vector Stores**: ChromaDB-based vector stores for each course (ML, SC, IoT) containing embedded lecture materials
- **Course Configuration** (`load_course_specific.py`): Dynamic loading of course-specific system prompts and vector stores

**Key Features:**
- Streaming chat responses for real-time interaction
- Session-based conversation history management
- Course-specific knowledge retrieval
- Feedback collection system for continuous improvement
- Multi-course support (ML, SC, IoT)

**Tech Stack:**
- Backend: Python, FastAPI, LangChain, ChromaDB
- Frontend: Next.js, React, TypeScript, Tailwind CSS
- Models: Fine-tuned Mistral, Codestral, Llama Cloud

### 🔬 `arete_workshop`

The workshop folder contains experimental code, research scripts, and development tools for:

- **Model Fine-tuning**: Scripts for training and fine-tuning language models on course-specific datasets
- **Data Processing**: Tools for preparing training datasets and processing course materials
- **Experimentation**: Research notebooks and scripts for testing new approaches and model configurations
- **Evaluation**: Scripts for assessing model performance and response quality

**Note:** This folder is used for research and development purposes. The code here may be experimental and not production-ready.

---

## Getting Started

### Prerequisites

- Python 3.8+
- Node.js 18+
- MySQL database (for conversation logging)
- HuggingFace API token (for model access)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/koskath/arete.git
cd arete
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Install Node.js dependencies:
```bash
cd arete_deployment
npm install
```

4. Set up environment variables:
```bash
# Create a .env file with:
HF_TOKEN=your_huggingface_token
ALLOWED_ORIGINS=*
# Add database credentials and other configuration as needed
```

### Running the Application

1. Start the FastAPI backend:
```bash
cd arete_deployment
python app.py
```

2. Start the Next.js frontend (in a separate terminal):
```bash
cd arete_deployment
npm run dev
```

The application will be available at `http://localhost:80`

---

## License

This project is developed at Copenhagen Business School for educational and research purposes.

---

<div align="center">
  <img src="arete_deployment/public/cbs_logo.png" alt="CBS Logo" height="40">
</div>

