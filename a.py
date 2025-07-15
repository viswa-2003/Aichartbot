import streamlit as st
import google.generativeai as ai

# Set Page Configuration
st.set_page_config(page_title="", page_icon="", layout="centered")

# Set AI Key
API_KEY = "AIzaSyDMq-FS-HKh-aUDqVLGmY41b0aPl-grWb8"
ai.configure(api_key=API_KEY)

model = ai.GenerativeModel("gemini-1.5-pro")
chat = model.start_chat()

# Custom CSS for Green Glow and Green Input Text
st.markdown("""
    <style>
    body {
        background-color: black; /* Full black background */
        color: white;
        font-family: 'Arial', sans-serif;
    }
    .stApp {
        background-color: #121212; /* Dark Grey Inner Box */
        padding: 20px;
        border-radius: 15px;
        border: 5px solid rgba(0, 255, 0, 0.9); /* Thicker Green Glow */
        box-shadow: 0px 0px 45px rgba(0, 255, 0, 1); /* Stronger and Wider Glow */
        max-width: 750px; /* Matches Input Box Width */
        margin: auto; /* Centers the chat box */
    }
    .chat-container {
        max-width: 700px;
        margin: auto;
        padding: 15px;
    }
    .chat-bubble {
        border-radius: 15px;
        padding: 12px 18px;
        margin-bottom: 10px;
        max-width: 80%;
        word-wrap: break-word;
    }
    .user {
        background: linear-gradient(to right, #00FF00, #33FF33);
        color: white;
        align-self: flex-end;
    }
    .assistant {
        background: #333;
        color: white;
        align-self: flex-start;
    }
    /* Fixed Input Bar to Match Green Edge */
    .stChatInput input {
        width: 750px !important; /* Same as Chat Box */
        background: #222 !important;
        color: #00FF00 !important; /* Green Typing Text */
        border-radius: 15px !important;
        padding: 12px !important;
        border: 3px solid #00FF00 !important; /* Green Border */
        box-shadow: 0px 0px 20px #00FF00 !important; /* Stronger Glow */
        font-size: 16px !important;
        margin: auto !important; /* Centers Input Box */
        display: block !important;
        text-align: left !important;
    }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("<h1 style='text-align: center;'> 💡Vijay AI ChatGpt </h1>", unsafe_allow_html=True)
st.write("💬 Chat with vijay AI in a  modern interface.")

# Chat History Storage
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Previous Messages with Custom Chat Bubbles
for msg in st.session_state.messages:
    role_class = "user" if msg["role"] == "user" else "assistant"
    role_label = "👤 You" if msg["role"] == "user" else "🤖 AI"
    st.markdown(f"""
        <div class='chat-container'>
            <div class='chat-bubble {role_class}'>
                <b>{role_label}:</b><br> {msg['text']}
            </div>
        </div>
    """, unsafe_allow_html=True)

# User Input
user_input = st.chat_input("💬 Type your message...")
if user_input:
    # Display User Message
    st.session_state.messages.append({"role": "user", "text": user_input})
    st.markdown(f"""
        <div class='chat-container'>
            <div class='chat-bubble user'>
                <b>👤 You:</b><br> {user_input}</br>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Get AI Response
    try:
        response = chat.send_message(user_input)
        ai_reply = response.text
    except Exception as e:
        ai_reply = "⚠️ Error connecting to AI. Please check API key and model name."

    # Display AI Response
    st.session_state.messages.append({"role": "assistant", "text": ai_reply})
    st.markdown(f"""
        <div class='chat-container'>
            <div class='chat-bubble assistant'>
                <b>🤖 AI:</b><br> {ai_reply}</br>
            </div>
        </div>
    """, unsafe_allow_html=True)
