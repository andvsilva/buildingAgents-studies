import streamlit as st
from prompts.strategies import zero_shot, few_shot, cot, tot
from chains.engine import run_prompt

st.set_page_config(page_title="Prompt Engineering Lab")
st.title("🧠 Prompt Engineering Lab")

question = st.text_area("Enter your question")

strategy = st.selectbox(
    "Choose Prompt Strategy",
    ["Zero-Shot", "Few-Shot", "Chain-of-Thought", "Tree-of-Thought"]
)

temperature = st.slider("Temperature", 0.0, 1.0, 0.0)

if st.button("Run Experiment"):
    if not question.strip():
        st.warning("Digite uma pergunta antes de executar.")
    else:
        if strategy == "Zero-Shot":
            prompt = zero_shot(question)
        elif strategy == "Few-Shot":
            prompt = few_shot(question)
        elif strategy == "Chain-of-Thought":
            prompt = cot(question)
        else:
            prompt = tot(question)

        response = run_prompt(prompt, temperature)

        st.subheader("Response")
        st.text_area("Output", value=response, height=300, key="response_area")

        # Botão seguro para copiar ou baixar a resposta
        st.download_button(
            label="Copy / Download Response",
            data=response,
            file_name="response.txt",
            mime="text/plain"
        )