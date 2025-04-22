# import gradio as gr
# import requests

# API_URL = "http://localhost:8000/chat"

# def chat_fn(message, history, model):
#     payload = {
#         "message": message,
#         "session_id": "test-session",
#         "model": model
#     }

#     try:
#         response = requests.post(API_URL, json=payload)
#         response.raise_for_status()  # Raise error for non-200
#         bot_response = response.json().get("response", "No response field in JSON")
#         history.append((message, bot_response))
#         return history
#     except Exception as e:
#         history.append((message, f"[Error] {str(e)}"))
#         return history

# with gr.Blocks() as demo:
#     gr.Markdown("## Conversational AI Chat")
#     model = gr.Dropdown(["gemini", "openai", "claude", "mistral"], label="Select LLM", value="gemini")
#     chatbot = gr.Chatbot()
#     msg = gr.Textbox()
#     msg.submit(chat_fn, [msg, chatbot, model], chatbot)

# demo.launch()
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
        return history, ""  # Return an empty string to clear the input field
    except Exception as e:
        history.append((message, f"[Error] {str(e)}"))
        return history, ""  # Return an empty string to clear the input field

with gr.Blocks() as demo:
    gr.Markdown(
        """
        <h1 style="text-align: center; font-family: Arial, sans-serif; color: #4CAF50;">
            Conversational AI Chat
        </h1>
        """,
    )

    model = gr.Dropdown(["gemini", "openai", "claude", "mistral"], label="Select LLM", value="gemini")
    chatbot = gr.Chatbot()
    msg = gr.Textbox(placeholder="Type your message here...")

    msg.submit(chat_fn, [msg, chatbot, model], [chatbot, msg])

demo.launch()
