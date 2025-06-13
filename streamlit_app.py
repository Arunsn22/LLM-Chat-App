import streamlit as st
import requests

# Page configuration
st.set_page_config(page_title="Chat with Local LLM", page_icon="🤖", layout="centered")

# Inject custom CSS for styling
st.markdown("""
    <style>
    body {
        background-color: #0d6efd;
    }
    .chat-bubble-user {
        background-color: #0d6efd;
        padding: 0.8rem;
        border-radius: 0.8rem;
        margin-bottom: 0.5rem;
        align-self: flex-start;
        width: fit-content;
        max-width: 85%;
    }
    .chat-bubble-bot {
        background-color: #0d6efd;
        padding: 0.8rem;
        border-radius: 0.8rem;
        margin-bottom: 0.5rem;
        align-self: flex-end;
        width: fit-content;
        max-width: 85%;
        border-left: 4px solid #0d6efd;
    }
    .chat-container {
        display: flex;
        flex-direction: column;
    }
    .header {
        background: linear-gradient(90deg, #0d6efd, #6610f2);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 20px;
        font-size: 24px;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="header">🤖 LLM Chat Bot 🤖</div>', unsafe_allow_html=True)

# Submit function
def on_submit():
    user_message = st.session_state.user_message_input.strip()
    st.session_state.user_message_input = ""  # Clear it first to avoid showing in next rerun

    if user_message:
        try:
            # Send request first
            print(">> Sending POST request to FastAPI backend")
            response = requests.post(
                "http://localhost:8000/chat",
                json={"user_message": user_message},
                timeout=180
            )
            print(f">> Received HTTP Response: {response}")
            data = response.json()
            bot_response = data.get("response", "No response from the server.")

            # Append both user and bot message only once
            st.session_state.chat_history.append(("user", user_message))
            st.session_state.chat_history.append(("bot", bot_response))
        except requests.exceptions.RequestException as e:
            st.session_state.chat_history.append(("user", user_message))
            st.session_state.chat_history.append(("bot", f"⚠️ Failed to get response: {e}"))

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "user_message_input" not in st.session_state:
    st.session_state.user_message_input = ""

# Display chat in styled bubbles
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for sender, message in st.session_state.chat_history:
    alignment = "flex-end" if sender == "user" else "flex-start"
    bubble_color = "#0d6efd" if sender == "user" else "#6610f2"
    text_color = "white"

    html = f"""
        <div style="display: flex; justify-content: {alignment}; padding: 4px 0;">
            <div style="
                background-color: {bubble_color};
                color: {text_color};
                padding: 10px 16px;
                border-radius: 12px;
                max-width: 80%;
                word-wrap: break-word;
                ">
                {message}
            </div>
        </div>
    """
    st.markdown(html, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Input box remains at bottom
st.text_input("Ask away...", key="user_message_input", on_change=on_submit)
