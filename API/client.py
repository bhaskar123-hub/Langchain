import requests
import streamlit as st

# Function to get response from the FastAPI server for essay generation (using Gemma2.2b model)
def get_gemma_response(input_text):
    try:
        response = requests.post(
            "http://localhost:8000/essay/invoke",  # Route for Gemma model
            json={'input': {'topic': input_text}}
        )
        response.raise_for_status()
        
        # Debugging: print the entire response to inspect the structure
        #st.write(f"Response from Gemma: {response.json()}")
        
        # Extract content from the correct field in response
        content = response.json().get('output', {}).get('text', "Error: Text not found in response")
        return content
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

# Function to get response from the FastAPI server for poem generation (using Llama3.2 model)
def get_llama_response(input_text):
    try:
        response = requests.post(
            "http://localhost:8000/poem/invoke",  # Route for Llama model
            json={'input': {'topic': input_text}}
        )
        response.raise_for_status()
        
        # Debugging: print the entire response to inspect the structure
        #st.write(f"Response from Llama: {response.json()}")
        
        # Extract content from the correct field in response
        content = response.json().get('output', {}).get('text', "Error: Text not found in response")
        return content
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.title('Langchain Demo With Gemma2.2b and Llama3.2 API')

# Text inputs for essay and poem topics
input_text = st.text_input("Write an essay on")
input_text1 = st.text_input("Write a poem on")

# Handling essay request for Gemma2.2b model
if input_text.strip():
    st.write(get_gemma_response(input_text))  # Get essay content from Gemma
else:
    if input_text:
        st.warning("Please enter a valid topic for the essay.")

# Handling poem request for Llama3.2 model
if input_text1.strip():
    st.write(get_llama_response(input_text1))  # Get poem content from Llama
else:
    if input_text1:
        st.warning("Please enter a valid topic for the poem.")
