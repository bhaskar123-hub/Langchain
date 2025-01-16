from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
from langchain.chains import LLMChain
from langchain_ollama import OllamaLLM  # Import OllamaLLM from langchain-ollama

app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API Server"
)

# Ollama model for Gemma2.2b
gemma_llm = OllamaLLM(model="gemma2:2b")  # Using Gemma2.2b model here

# Ollama model for Llama3.2
llama_llm = OllamaLLM(model="llama3.2")  # Using Llama3.2 model

# Define prompts for essay and poem
prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2 = ChatPromptTemplate.from_template("Write me a poem about {topic} for a 5-year-old child with 100 words")

# Combine the prompt and the LLM into a chain
essay_chain = LLMChain(llm=gemma_llm, prompt=prompt1)
poem_chain = LLMChain(llm=llama_llm, prompt=prompt2)

# Add routes
add_routes(
    app,
    essay_chain,
    path="/essay"
)

add_routes(
    app,
    poem_chain,
    path="/poem"
)

# Run the FastAPI app
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
