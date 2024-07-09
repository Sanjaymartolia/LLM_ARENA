import os
from dotenv import load_dotenv
from langchain_community.llms import Llama 
from langchain.llms import Llama, Mistral, Gemini, Claude  

load_dotenv()

def load_llama3_70b():
    api_key = os.getenv("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")
    return Llama(api_key=api_key, model_name="llama3-70b")

def load_mistral():
    api_key = os.getenv("3YN7uxockgiLkqNQU7tPDLNKcIdR9eYc")
    return Mistral(api_key=api_key)

def load_gemini():
    api_key = os.getenv("AIzaSyC21dHX3tnBgqX_EvlOfz_VPqoAMpyORHc")
    return Gemini(api_key=api_key)

def load_claude():
    api_key = os.getenv("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")
    return Claude(api_key=api_key)

# Add more functions for other LLMs if needed
