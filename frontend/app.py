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
    model = gr.Dropdown(["gemini", "openai", "claude", "mistral"], label="Select LLM", value="gemini")
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    msg.submit(chat_fn, [msg, chatbot, model], chatbot)

demo.launch()
