import gradio as gr
from chatbot_functions import DataProcessor, Chatbot

# Initialize data and chatbot
data_processor = DataProcessor()  # loads cleaned_medquad.csv
chatbot = Chatbot(data_processor)

# Gradio function
def chat_with_backend(message):
    if not message.strip():
        return "Please enter a question."
    
    best_question, response, source = chatbot.get_response(message)
    if best_question == "UNKNOWN":
        return response
    else:
        return f"Matched question: {best_question}\nAnswer: {response}\nSource: {source}"

# Gradio interface
iface = gr.ChatInterface(
    fn=chat_with_backend,
    title="Care Companion Chatbot",
    description="Ask health-related questions and get reliable answers from Care Companion."
)

if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0", server_port=7860, debug=True)
