import gradio as gr
import requests

API_URL = "https://carecompanion-chatbotpython-chatbot-app.onrender.com/chat"

def chat_with_backend(message):
    if not message.strip():
        return "Please enter a question."
    try:
        payload = {"user_input": message}
        response = requests.post(API_URL, json=payload)
        # Print for debugging
        print("Status code:", response.status_code)
        print("Response text:", response.text)
        
        if response.status_code == 200:
            data = response.json()
            print("JSON response:", data)
            return data.get("response", "No response from bot.")
        else:
            return f"Error {response.status_code}: {response.text}"
    except Exception as e:
        return f"Exception occurred: {str(e)}"

iface = gr.ChatInterface(
    fn=chat_with_backend,
    title="Care Companion Chatbot",
    description="Ask health-related questions and get reliable answers from Care Companion."
)

if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0", server_port=7860, debug=True)

