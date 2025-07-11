import streamlit as st
import os
import requests

# Set API key
api_key = "4141f2d62dc1abfc5533c7756bbdc12fc8862a85db140eaec63adc83efa97a5d"

# Set API endpoint and model
endpoint = "https://api.together.xyz/v1/chat/completions"
model = "mistralai/Mixtral-8x7B-Instruct-v0.1"

# Set background image
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("https://raw.githubusercontent.com/akashBv6680/ashwinai/main/white.png");
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

def get_response(query):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "messages": [{"role": "user", "content": query}],
        "max_tokens": 512,
        "temperature": 0
    }
    response = requests.post(endpoint, headers=headers, json=data)
    if response.status_code == 200:
        response_json = response.json()
        return response_json["choices"][0]["message"]["content"]
    else:
        return "Error: " + str(response.status_code)

def main():
    st.title("HELLO I'M BHEEMA AI Chatbot")
    query = st.text_input("You: ")
    if query:
        response = get_response(query)
        st.write("BHEEMA AI: ", response)

if __name__ == "__main__":
    main()
