# Local-chatGPT

This project provides a 100% locally running chatbot that leverages Google DeepMind's `gemma4:e2b` model. It uses Streamlit to create an interactive, ChatGPT-like interface and Ollama to serve the model. The assistant is configured with a unique 'Sherlock' persona—analytical, sarcastic, and helpful.

## Features

- **Runs Locally**: Your conversations are private and processed entirely on your machine.
- **Multimodal**: Supports both text and image-based (PNG, JPG, JPEG) queries.
- **Interactive UI**: A clean, conversational interface built with Streamlit.
- **Streaming Responses**: Receives and displays the AI's response in real-time for a dynamic user experience.
- **Custom Persona**: Chat with 'Sherlock', a brilliant and witty AI assistant defined by a custom system prompt.
- **Conversation History**: Maintains the context of the conversation within a session.

## Getting Started

Follow these instructions to get the chatbot running on your local machine.

### Prerequisites

Before you begin, ensure you have the following installed:
- [Python 3.8+](https://www.python.org/downloads/)
- [Ollama](https://ollama.com/)

You also need to pull the `gemma4:e2b` model using Ollama. Open your terminal and run:
```bash
ollama pull gemma4:e2b
```
Ensure the Ollama application is running before proceeding to the next step.

### Installation & Running

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/tanmayymishra/Local-chatGPT.git
    cd Local-chatGPT
    ```

2.  **Install the required Python packages:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

Your browser should automatically open a new tab with the chatbot interface. You can now start a conversation with Sherlock!
