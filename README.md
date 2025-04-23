# 🧠 Conversational AI Chat App (FastAPI + Gradio + Gemini)

This is a production-ready Conversational AI application built as part of a 24-hour challenge for Yuñ. It uses **FastAPI** for the backend MCP server, **Gradio** for a clean chat frontend, and supports LLM integration including **Google Gemini**, **OpenAI**, and open-source models like **Mistral**.

---

## ⚙️ Features

- ✅ Conversational AI via Google Gemini (default)
- 🔄 Switch between LLMs like OpenAI, Claude, and Mistral
- 💬 Context-aware chat via FastAPI and Gradio
- 🐳 Dockerized backend & frontend
- 🚀 Runs locally and deploys easily

---

## 🧱 Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/) – Backend server
- [Gradio](https://www.gradio.app/) – Frontend UI
- [Google Generative AI](https://ai.google.dev/) – Gemini model
- [Docker & Docker Compose](https://docs.docker.com/) – Containerization
- Python 3.11

---

## 🚀 Run Locally with Docker

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/conversational-ai-app.git
cd conversational-ai-app

2. Create .env File
In the root of the project:

touch .env
Then add your Gemini API key:
GEMINI_API_KEY=your-google-gemini-api-key

3. Build & Start the App
docker-compose up --build

4. Access the App
🧠 Gradio Chat UI: http://localhost:7860

⚙️ FastAPI Docs: http://localhost:8000/docs

📁 Folder Structure

conversational-ai-app/
├── backend/         # FastAPI backend server (MCP)
│   ├── main.py
│   ├── mcp/
│   ├── llms/
│   ├── utils/
│   └── Dockerfile
│
├── frontend/        # Gradio frontend
│   ├── app.py
│   └── Dockerfile
│
├── docker-compose.yml
├── requirements.txt
├── .env (not tracked)
├── .gitignore
└── README.md


🛠️ LLM Support
Switch LLMs by selecting from the dropdown in the UI:

gemini (default)

openai

claude (stub only)

mistral (stub or real if integrated)

🧪 Requirements
✅ Docker

✅ Docker Compose

✅ Google Gemini API Key
Get it here → https://ai.google.dev/gemini-api/docs/api-key