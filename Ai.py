import os
import requests
import streamlit as st

# Load API key securely from Streamlit secrets
api_key = st.secrets["GEMINI_API_KEY"]

# Set Gemini model name
# Options: "gemini-2.5-flash", "gemini-2.0-flash", or "gemini-1.5-flash"
model = "gemini-2.5-flash"
endpoint = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"

# Set custom styling and background
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://raw.githubusercontent.com/akashBv6680/ashwinai/main/white.png");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def get_response(query):
    headers = {"Content-Type": "application/json"}
    params = {"key": api_key}
    data = {"contents": [{"parts": [{"text": query}]}]}

    try:
        response = requests.post(endpoint, headers=headers, params=params, json=data)
        
        if response.status_code == 200:
            response_json = response.json()
            return response_json["candidates"][0]["content"]["parts"][0]["text"]
        else:
            return f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"An error occurred: {str(e)}"


def main():
    st.title("HELLO I'M BHEEMA AI Chatbot")
    query = st.text_input("You: ")
    if query:
        response = get_response(query)
        st.write("BHEEMA AI: ", response)


if __name__ == "__main__":
    main()
