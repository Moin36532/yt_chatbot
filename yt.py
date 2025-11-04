import streamlit as st
from ytvideo_chatbot import chain_final
st.set_page_config(page_title="🎬 YouTube Video Chatbot", layout="centered")

st.title("🎬 YouTube Video Chatbot")
st.write("Ask questions about any YouTube video!")



url = st.text_input("YouTube Video URL")
question = st.text_area("Your question")
if st.button('submit'):
    result = chain_final.invoke({'URL': url,'question':question})
    st.write(result.content)
