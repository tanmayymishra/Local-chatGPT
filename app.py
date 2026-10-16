import streamlit as st
import ollama

SYSTEM_PROMPT = [
    {
        "role": "system",
        "content": (
            "You are 'Sherlock', a brilliantly analytical, mildly sarcastic, "
            "yet incredibly helpful AI assistant. You solve problems like detective cases, "
            "using keen observation and logical deduction. Keep answers precise."
        ),
    },
    {
        "role": "assistant",
        "content": "Hello, Sherlock this side. How can I help you today?",
    },
]
# Session State Initialization
if "interaction" not in st.session_state:
    st.session_state.interaction = list(SYSTEM_PROMPT)

st.title("Local Gemma 4 Chatbot")

# Render Chat History
for msg in st.session_state.interaction:
    # Skip rendering the invisible system prompt
    if msg["role"] == "system":
        continue

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

        # If the user previously uploaded an image, display it in the history
        if msg.get("images"):
            st.image(msg["images"][0])

# Image Upload
uploaded_file = st.file_uploader(
    "Attach an image (optional)", type=["png", "jpg", "jpeg"]
)

# Handle New User Input
prompt = st.chat_input("Ask me anything...")
if prompt:

    # Render user's new message in the UI immediately
    with st.chat_message("user"):
        st.markdown(prompt)
        if uploaded_file:
            st.image(uploaded_file)

    # Prepare the user message payload
    user_message = {"role": "user", "content": prompt}

    # If an image was uploaded, read it as bytes and attach it
    if uploaded_file:
        img_bytes = uploaded_file.getvalue()
        user_message["images"] = [img_bytes]

    # Append to session state
    st.session_state.interaction.append(user_message)

    #  Generate and Stream Response
    with st.chat_message("assistant"):

        # Call Ollama with stream=True
        response_stream = ollama.chat(
            model="gemma4:e2b", messages=st.session_state.interaction, stream=True
        )

        # Helper function to extract text chunks from Ollama's stream
        def generate_chunks():
            for chunk in response_stream:
                yield chunk["message"][
                    "content"
                ]  # yield pauses the function, sends the current piece of text out to the caller, and waits for the loop to fetch the next chunk.

        # st.write_stream natively handles the typewriter effect
        full_response = st.write_stream(generate_chunks())

    # Append the final assistant response to the conversation history
    st.session_state.interaction.append({"role": "assistant", "content": full_response})
