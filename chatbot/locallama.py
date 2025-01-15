# Importing necessary libraries for the application
import os  # For interacting with the operating system (environment variables)
import streamlit as st  # Streamlit is used to create interactive web applications
from langchain.prompts import ChatPromptTemplate  # Importing the ChatPromptTemplate for prompt generation
from langchain_openai import ChatOpenAI  # Importing the OpenAI-specific LLM integration
from langchain_community.llms import Ollama  # Importing the Ollama LLM integration for local models

# Set environment variables for Langsmith and OpenAI API keys
# These environment variables are used to enable Langsmith tracing and set up the LangChain API integration
os.environ["LANGSMITH_TRACING"] = "true"  # Enables tracing for Langsmith
os.environ["LANGSMITH_ENDPOINT"] = "https://api.smith.langchain.com"  # URL endpoint for Langsmith API
os.environ["LANGSMITH_API_KEY"] = "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"  # API key for Langsmith
os.environ["LANGSMITH_PROJECT"] = "MyLearning"  # Project name for Langsmith usage
os.environ["OPENAI_API_KEY"] = "<your-openai-api-key>"  # OpenAI API key to enable OpenAI LLMs (replace with your key)

## Creating the Chat Prompt Template
# A template for generating prompts in a conversational format.
# It will help structure the conversation, like system instructions and user inputs.
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries."),  # System-level instruction for the model
        ("user", "Question: {question}")  # The user input placeholder for the model's response
    ]
)

## Streamlit framework for building the web app
st.title('Langchain Demo With LLAMA3 API')  # Setting the title of the web app

# Creating an input box in the web app to capture user queries
input_text = st.text_input("Search the topic you want")  # User will enter the question in this box

# Ollama model integration with LangChain
# This loads the Llama model from Ollama's local system for use in the LangChain pipeline
llm = Ollama(model="llama3.2")  # Make sure you are using the correct model identifier ("llama3.2")

# Building the LangChain processing chain:
# The prompt and the LLM are combined to form the pipeline. 
# The chain connects the input to the model through the prompt template.
chain = prompt | llm 

# Checking if the user has provided an input in the text box
if input_text:
    # The chain is invoked with the user input, and it generates a response.
    response = chain.invoke({"question": input_text})  # The input text is passed as a question to the LLM
    st.write(response)  # Display the model's response in the Streamlit app
