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
- **Live service:** [arete.cbs.dk](https://arete.cbs.dk)
- **LinkedIn:** [Konstantinos Katharakis](https://www.linkedin.com/in/konstantinos-katharakis)
- **Institution:** [Copenhagen Business School - Department of Digitalisation](https://www.cbs.dk/en/research/departments/department-digitalisation)

---

## Project Structure

```
arete/
├── arete_deployment/     # the live service (backend + frontend)
├── finetuning/           # model training (SFT and DPO)
├── vectorstores/         # course material and index building
├── system_messages/      # one system prompt per course
└── arete_workshop/       # experiments, not production
```

### `arete_deployment`

The production-ready application:

- **Backend API** (`app.py`): FastAPI REST API that handles chat requests, streaming responses, and conversation management
- **Frontend Application** (`app/`): Next.js React application with TypeScript providing the chat interface
- **RAG Pipeline** (`rag_pipeline.py`): retrieves the relevant slides from the vector store and builds the prompt sent to the model
- **Model Integration** (`instruct_model.py`): interfaces with the model providers (HuggingFace endpoints, Mistral, Codestral)
- **Course Configuration** (`load_course_specific.py`): loads the system prompt and vector store for the requested course
- **Logging** (`sql_related.py`): saves every question and answer to MySQL and records the like/dislike feedback

**Key Features:**
- Streaming chat responses for real-time interaction
- Session-based conversation history management
- Course-specific knowledge retrieval with source citations
- Feedback collection system for continuous improvement
- Multi-course support (ML, SC, IoT)

**Tech Stack:**
- Backend: Python, FastAPI, LangChain, ChromaDB
- Frontend: Next.js, React, TypeScript, Tailwind CSS
- Models: Fine-tuned Mistral, Codestral, Llama Cloud

### `finetuning`

Everything used to train the model:

- **`scripts/finetuning_lora.py`**: Supervised Fine-Tuning (SFT) with TRL and LoRA. This is what teaches the model to guide students instead of solving problems for them.
- **`scripts/fine_tuning_no_lora.py`**: the same step without LoRA, for comparison
- **`scripts/dpo_ft.py`**: Direct Preference Optimization (DPO) on top of the SFT model, using the like/dislike feedback as preference data
- **`scripts/merge_sft.py`** and **`scripts/merge_dpo.py`**: merge the LoRA adapters into the base model to produce a single standalone model
- **`scripts/upload_finetuning.py`**: pushes a merged model to the Hugging Face Hub
- **`datasets/`**: the question-and-answer pairs used for SFT, and the preference pairs used for DPO

**Note on DPO:** the DPO model was trained and tested successfully, but it is not the model in production. The managed provider used for hosting only serves supervised fine-tuned models.

### `vectorstores`

The RAG index and the course material it is built from:

- **`create_vec_op.py`**: builds a Chroma vector store using open-source embeddings (Qwen3-Embedding-0.6B)
- **`create_vec_mis.py`**: the same, using Mistral embeddings (codestral-embed)
- **`ML/`, `SC/`, `IoT/`**: the cleaned lecture material, one file per slide, named `lecture_<L>_slide_<S>` so the bot can cite its sources

### `system_messages`

One system prompt per course. Each one tells the model to give step-by-step guidance instead of full solutions, to cite the lecture and slide for each key point, and to refuse questions outside the course. The same prompts were used to generate the training data, so training and serving stay consistent.

### `arete_workshop`

Standalone example scripts used for teaching and experimentation. `api_runs/` shows a minimal chatbot built on the OpenAI API. `open_source_run/` shows the same thing with a locally hosted open-source model, in a terminal and in a Gradio web app.

**Note:** this folder is for research and demonstration. The code here is not part of the production service.

### Not included in this repository

- **Lecture slides in their original form.** Only teacher-made material could be used, and it is not ours to republish.
- **Built vector stores and model weights.** These are large and can be rebuilt from the scripts above.
- **Environment files.** See the setup instructions below for the variables you need.

---

## Getting Started

### Prerequisites

- Python 3.8+
- Node.js 18+
- MySQL database (for conversation logging)
- HuggingFace API token (for model access)
- Mistral API key (only if you use the Mistral embeddings or the Mistral-hosted model)
- A CUDA GPU (only for fine-tuning and for running the embedding model locally)

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

`requirements.txt` covers the deployment service. Fine-tuning needs a few more packages:
```bash
pip install trl peft datasets bitsandbytes accelerate
```

3. Install Node.js dependencies:
```bash
cd arete_deployment
npm install
```

4. Set up environment variables. Create a `.env` file in the repository root:
```bash
# Model access
HF_TOKEN=your_huggingface_token
MISTRAL_API_KEY=your_mistral_key           # for Mistral embeddings and model
MISTRAL_NEMO_FINETUNED=your_model_id       # the fine-tuned model to serve

# Database (conversation logging and feedback)
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_DB=arete
MYSQL_USER=your_user
MYSQL_PASSWORD=your_password

# API
ALLOWED_ORIGINS=*                          # restrict this in production
```

### Building the vector stores

The service needs a vector store per course before it can answer anything. Build them once:
```bash
cd vectorstores
python create_vec_op.py     # open-source embeddings, for ML and SC
python create_vec_mis.py    # Mistral embeddings, for IoT
```
Each script has the course name and output path set at the top. Edit those before running.

### Running the Application

1. Start the FastAPI backend (runs on port 8000):
```bash
cd arete_deployment
python app.py
```

2. Start the Next.js frontend in a separate terminal (runs on port 80):
```bash
cd arete_deployment
npm run dev
```

The application will be available at `http://localhost:80`. The frontend calls the backend, so both need to be running.

---

## License

This project is developed at Copenhagen Business School for educational and research purposes.

---

<div align="center">
  <img src="arete_deployment/public/cbs_logo.png" alt="CBS Logo" height="40">
</div>

