#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
import streamlit as st
import requests

# Config API Key and Model
OPEN_ROUTER_API_KEY= "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"
MODEL="openai/gpt-3.5-turbo"

HEADERS = {
    "Authorization": f"Bearer {OPEN_ROUTER_API_KEY}",
    "http-referer": "http://localhost:8501",
    "Content-Type": "application/json",
    "X-title": "AI Chatbot streamlit"
}

API_URL = "https://openrouter.ai/api/v1/chat/completions"

st.title("AI Chatbot with OpenRouter by Lathif Jumatiawan")
st.markdown(f"Powered by [OpenRouter](https://openrouter.ai) using model: **{MODEL}**")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.markdown(chat["content"])

user_input = st.chat_input("Type your message here...")
if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    with st.spinner("Thinking..."):
        payload = {
            "model": MODEL,
            "messages": [
                {"role": "user", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ],
            "max_tokens": 1000,
            "temperature": 0.7
        }

        response = requests.post(API_URL, headers=HEADERS, json=payload)

        if response.status_code == 200:
            bot_response = response.json()["choices"][0]["message"]["content"]
        else:
            bot_response = "No response from the model."

    st.chat_message("assistant").markdown(bot_response)
    st.session_state.chat_history.append({"role": "assistant", "content": bot_response})