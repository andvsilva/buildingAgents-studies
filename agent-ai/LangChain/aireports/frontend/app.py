import streamlit as st
import requests

st.title("💬 AI Financial Assistant")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("Your question:")

if st.button("Send") and user_input:
    response = requests.post(
        "http://127.0.0.1:8000/ask",
        json={"question": user_input}
    )

    answer = response.json()["answer"]

    st.session_state.history.append(
        {"user": user_input, "assistant": answer}
    )

for chat in st.session_state.history:
    st.markdown(f"**You:** {chat['user']}")
    st.markdown(f"**AI:** {chat['assistant']}")