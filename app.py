import streamlit as st
from llmware.configs import LLMWareConfig

from llm_backend import QA_sytem

LIBRARY_NAME = "compiler_design"
MODEL_NAME = "llmware/bling-tiny-llama-v0"

LLMWareConfig().set_active_db("sqlite")

# Title and Text Input
st.title("Wise Crack")
st.write("Welcome to Wise Crack, the question answering system! ")
st.write("Wise Crack is a simple question answering system made to help KTU students with their doubts in Computer Science subjects. Just ask your question and Wise Crack will do its best to answer it!")
st.write("Currently, Wise Crack is under development and only supports questions for the Compiler Design subject. More subjects will be added soon!")

user_question = st.text_input("Ask your question here:")

# Button and Answer Display
if st.button("Ask"):
  if user_question:
    answer = QA_sytem.prompt_with_sources(MODEL_NAME, LIBRARY_NAME, user_question)
    st.write(answer)
  else:
    st.write("Please enter a question.")
