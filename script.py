import streamlit as st
from llm import summarize_text
st.title("Quickry")

st.write(
    "Qickry AI is a AI based text summarizer for your long reads so that you can ge quick summary ."
)

user_input = st.text_area(
    "Enter your text here:",
    height=250,
    placeholder="Paste your paragraph or article here..."
)


summarize_button = st.button("Summarize")


if summarize_button:

    # Check empty input
    if user_input.strip() != "":

        # Loading spinner
        with st.spinner("Generating summary..."):

            # Call AI function
            summary = summarize_text(user_input)

        # Display output
        st.subheader("Summary Output")

        st.write(summary)

    else:
        st.warning("Please enter some text before summarizing.")