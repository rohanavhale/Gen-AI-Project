import streamlit as st
import os

st.set_page_config(
    page_title="GenAI Assistant",
    page_icon="🤖"
)

st.title("🤖 GenAI Assistant")
st.write("A simple Generative AI application deployed using Streamlit.")

st.sidebar.header("Settings")

user_name = st.sidebar.text_input(
    "Enter your name",
    value="User"
)

st.write(f"Hello, {user_name}! 👋")

question = st.text_area(
    "Enter your question:",
    placeholder="Ask something..."
)

if st.button("Generate Response"):

    if question.strip() == "":
        st.warning("Please enter a question.")

    else:
        # Demo response
        # Replace this section with your actual GenAI model/API
        response = f"""
        You asked:

        {question}

        This is a demo GenAI response.

        In the actual application, this section can be connected
        to an LLM such as OpenAI, Gemini, Hugging Face, or another
        cloud-accessible model.
        """

        st.subheader("Response")
        st.write(response)

st.divider()

st.caption("GenAI Deployment Assignment")