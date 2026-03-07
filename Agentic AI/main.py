import streamlit as st

from datetime import datetime

messages = st.session_state.get("messages", [])

if "messages" not in st.session_state:
    st.session_state["messages"] = messages

def get_greeting():
    current_hour = datetime.now().hour
    if 5 <= current_hour < 12:
        return "Good morning!"
    elif 12 <= current_hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"

st.title("Hello There! 👋")

name = st.text_input("What's your name?")
if name:
    user_message = st.chat_input("Type your message here...")
    if user_message:
        message = get_greeting() + " " + name 
        st.session_state["messages"] = messages + [{"role": "user", "content": user_message}, {"role": "assistant", "content": message}]

for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

#uv run streamlit run main.py
