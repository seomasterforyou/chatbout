import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Harry Chatbot", layout="centered")
st.title("💬 Harry's Chatbot")

# Pull API key from Streamlit secrets
API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

user_message = st.chat_input("Type your message…")

if user_message:
    with st.chat_message("user"):
        st.markdown(user_message)

    response = st.session_state.chat.send_message(user_message)

    with st.chat_message("assistant"):
        st.markdown(response.text)


