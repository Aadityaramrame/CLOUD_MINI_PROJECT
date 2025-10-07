import gradio as gr
import requests

API_URL = "https://carecompanion-chatbotpython-chatbot-app.onrender.com/chatbot"

def chat_with_backend(message):
    try:
        payload = {"user_input": message}
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            return response.json().get("bot_response", "No response from bot.")
        else:
            return f"Error {response.status_code}: {response.text}"
    except Exception as e:
        return f"Error: {str(e)}"

iface = gr.ChatInterface(fn=chat_with_backend, title="Care Companion Chatbot")

if __name__ == "__main__":
    iface.launch()
