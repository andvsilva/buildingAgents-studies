import streamlit as st

st.set_page_config(page_title="AI Financial Assistant", page_icon="💰")

st.title("💬 AI Financial Assistant")
st.write(
    "Type your financial question below."
)

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("Your question:")

if st.button("Send") and user_input:
    response = f"You asked: {user_input}"

    st.session_state.history.append(
        {"user": user_input, "assistant": response}
    )

for chat in st.session_state.history:
    st.markdown(f"**You:** {chat['user']}")
    st.markdown(f"**AI:** {chat['assistant']}")