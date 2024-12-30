from langchain_community.llms import HuggingFaceHub
import streamlit as st

# Function to load the answer using the Hugging Face endpoint
def load_answer(text):
    llm = HuggingFaceHub(
        repo_id="mistralai/Mistral-Nemo-Instruct-2407",huggingfacehub_api_token="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"
    )
    op = llm(text)
    return op

# Function to get user input
def get_text():
    input_text = st.text_input("you=", key="input")
    return input_text

# Streamlit app configuration
st.set_page_config(page_title="Simple chat app", page_icon=":robot:")
st.header("Llama 3 chat app")

# Get user input
user_input = get_text()
confirm = st.button("Generate")
if confirm and user_input:
    st.subheader("Answer")
    ans = load_answer(user_input)
    st.write(ans)
    st.balloons()
