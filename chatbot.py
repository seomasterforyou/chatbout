import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Gemini Chatbot", layout="centered")
st.title("💬 Gemini Chatbot")

API_KEY = st.secrets["AIzaSyBWka9iF-Y2IQ_Aoi1SUfY6SpVKVktfHCs"]   # pulled from secrets
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
