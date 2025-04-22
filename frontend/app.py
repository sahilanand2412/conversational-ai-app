import gradio as gr
import requests

API_URL = "http://localhost:8000/chat"

def chat_fn(message, history, model):
    payload = {
        "message": message,
        "session_id": "test-session",
        "model": model
    }

    try:
        response = requests.post(API_URL, json=payload)
        response.raise_for_status()  # Raise error for non-200
        bot_response = response.json().get("response", "No response field in JSON")
        history.append((message, bot_response))
        return history
    except Exception as e:
        history.append((message, f"[Error] {str(e)}"))
        return history

with gr.Blocks() as demo:
    gr.Markdown("## Conversational AI Chat")
    model = gr.Dropdown(["gemini", "openai", "claude", "mistral"], label="Select LLM", value="gemini")
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    msg.submit(chat_fn, [msg, chatbot, model], chatbot)

demo.launch()
