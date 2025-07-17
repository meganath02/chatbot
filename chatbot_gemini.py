import streamlit as st
import google.generativeai as genai
from streamlit_chat import message

# =============================
# 🎯 CONFIGURE YOUR API KEY
# =============================
API_KEY = "AIzaSyDb1RYbGJde7acBwZDHvkZgyLOt3XFuXXo"  # Replace with your Google AI Studio key
genai.configure(api_key=API_KEY)

# =============================
# 🎯 MODEL SETUP
# =============================
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")
chat = model.start_chat(history=[])

# =============================
# 🎯 STREAMLIT PAGE SETUP
# =============================
st.set_page_config(page_title="Gemini AI Chat", page_icon="💬", layout="wide")

st.markdown("""
    <style>
        .main {background-color: #f4f4f9;}
        .stChatMessage {background-color: white; border-radius: 10px; padding: 10px; margin: 5px;}
        .st-emotion-cache-1n76uvr {max-height: 700px; overflow-y: scroll;}
    </style>
""", unsafe_allow_html=True)

st.title("🤖 My ChatBot")
st.markdown("Ask anything and get smart responses in real-time!")

# =============================
# 🎯 SESSION STATE SETUP
# =============================
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# =============================
# 🎯 CHAT UI
# =============================
def display_chat():
    for i, (sender, msg) in enumerate(st.session_state.chat_history):
        is_user = sender == "user"
        message(msg, is_user=is_user, key=f"{sender}_{i}", avatar_style="bottts" if not is_user else "personas")

display_chat()

# =============================
# 🎯 USER INPUT & RESPONSE
# =============================
user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.chat_history.append(("user", user_input))

    with st.spinner("I am  thinking..."):
        try:
            response = chat.send_message(user_input)
            st.session_state.chat_history.append(("bot", response.text))
        except Exception as e:
            st.error(f"❌ Error: {e}")

    st.rerun()
