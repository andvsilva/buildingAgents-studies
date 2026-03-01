import streamlit as st
import requests
import json

API_URL = "http://localhost:8000/ask"

st.set_page_config(
    page_title="AI Business Intelligence Assistant",
    layout="wide"
)

st.title("📊 AI Business Intelligence Assistant")

st.markdown(
    """
Ask questions about:
- 📈 Sales data (SQL)
- 📄 Company documents (RAG)
- 🔥 Hybrid business insights
"""
)

# Sidebar options
st.sidebar.header("Settings")

explain_mode = st.sidebar.checkbox("Explain Mode", value=False)

question = st.text_area(
    "Enter your question:",
    height=100,
    placeholder="Example: What was total revenue in January?"
)

if st.button("Ask", use_container_width=True):

    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):

            payload = {
                "question": question,
                "explain": explain_mode
            }

            try:
                response = requests.post(API_URL, json=payload)
                data = response.json()

                st.subheader("📌 Answer")
                st.write(data.get("answer", "No response"))

                # Explain Mode Section
                if explain_mode and "tools_used" in data:
                    st.divider()
                    st.subheader("🛠 Tools Used")

                    for tool in data["tools_used"]:
                        with st.expander(f"Tool: {tool['tool']}"):
                            st.markdown("**Input:**")
                            st.code(tool["input"], language="sql")

                            st.markdown("**Output:**")
                            st.code(tool["output"])

                    if "metadata" in data:
                        st.divider()
                        st.subheader("⏱ Execution Metadata")
                        st.json(data["metadata"])

            except Exception as e:
                st.error(f"Error: {e}")