import gradio as gr
import requests

API_URL = "http://localhost:8000/chat"

def chat_fn(message, history, model):
    payload = {
        "message": message,
        "session_id": "test-session",
        "model": model
    }
    response = requests.post(API_URL, json=payload)
    return response.json()["response"]

with gr.Blocks() as demo:
    gr.Markdown("## Conversational AI Chat")
    model = gr.Dropdown(["openai", "gemini", "claude"], label="Select LLM", value="openai")
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    msg.submit(chat_fn, [msg, chatbot, model], chatbot)

demo.launch()
