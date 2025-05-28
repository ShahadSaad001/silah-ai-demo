# Silah AI Demo

This repository contains a basic demonstration of how we are experimenting with AI models as part of our graduation project **Silah**. It includes simple examples of:

- Using Facebook Prophet for demand forecasting (still a work in progress)
- Using LaBSE (Language-agnostic BERT Sentence Embedding) for semantic similarity (currently a minimal demo)
- Using FastAPI to provide a simple API interface to these models

The code here is intended as a starting point and a way for the team to explore and understand how these models work together. It is not meant to be a complete or polished application.

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/ShahadSaad001/silah-ai-demo.git
cd silah-ai-demo
```

### 2. Create a Virtual Environment

We use `.venv`:

```bash
python -m venv .venv
```

Activate it:

- On **Windows**:

```bash
  .venv\Scripts\activate
```

- On **Linux/macOS**:

```bash
source .venv/bin/activate
```

You should now see `(.venv)` at the beginning of your terminal prompt.

---

### 3. Install Required Packages

Once inside the virtual environment, install the required dependencies:

```bash
pip install -r requirements.txt
```

---

### 4. Run the FastAPI Server

You can run the server using:

```bash
uvicorn main:app --reload
```

After that, open your browser and go to:

```arduino
http://127.0.0.1:8000/docs
```

This will open the interactive **Swagger UI** to test your endpoints.

---

## Files Overview

| File Name          | Description                                                                                                                              |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `main.py`          | FastAPI entry point that exposes two endpoints to test the Prophet and LaBSE models                                                      |
| `prophet_model.py` | Initial experimentation with Facebook Prophet (The model is not fitted yet)                                                              |
| `labse_model.py`   | Loads the LaBSE model and returns embeddings for a given input text (Currently a basic demo without advanced search or comparison logic) |
| `requirements.txt` | List of all Python dependencies for the project                                                                                          |
| `README.md`        | This file, which is setup guide and project summary                                                                                      |

---

## Libraries Used

- `fastapi` – web framework to build APIs
- [`uvicorn`](https://www.uvicorn.org/) – ASGI server to run FastAPI
- `prophet` – for time series forecasting
- `pandas` – for data loading and manipulation
- [`matplotlib`](https://matplotlib.org/) – for plotting (optional for Prophet)
- [`torch`](https://pytorch.org/) – required for LaBSE
- [`sentence-transformers`](https://www.sbert.net/) – for downloading and using the LaBSE model
