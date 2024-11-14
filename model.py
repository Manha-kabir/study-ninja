# model.py
import dotenv
import google.generativeai as genai
import streamlit as st

# Configure the API key for the generative AI
gemini_api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=gemini_api_key)

# Define the generation configuration
generation_config = {
    "temperature": 0.4,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
}

def model(info, history):
    # Format history for Google Generative AI
    formatted_history = []
    for item in history:
        role = "user" if item["role"] == "user" else "model"
        formatted_history.append({
            "role": role,
            "parts": [{"text": item["content"]}]
        })

    # Create the model with the specified generation configuration
    generative_model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )
    
    # Start or continue the chat session with history
    chat_session = generative_model.start_chat(history=formatted_history)

    # Prepare the message with system instruction and user query
    message = f"""
    put your system instruction here
    {info}
    """

    # Get the response from the model
    response = chat_session.send_message(message)
    response_text = response.text

    return response_text