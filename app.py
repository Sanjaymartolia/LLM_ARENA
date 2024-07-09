import streamlit as st
from LLMs import load_llama3_70b,  load_mistral, load_gemini, load_claude

# Load models
llama3_70b_model = load_llama3_70b()
mistral_model = load_mistral()
gemini_model = load_gemini()
claude_model = load_claude()

# UI with Streamlit
st.title("LLM Arena")
st.write("Select a model and enter your query:")

models = {
    "Llama3-70b": llama3_70b_model,
    "Mistral": mistral_model,
    "Gemini": gemini_model,
    "Claude": claude_model,
    
}

model_choice = st.selectbox("Choose a model", list(models.keys()))
query = st.text_input("Enter your query")

if st.button("Get Response"):
    model = models[model_choice]
    response = model.generate(query)  # Adjust based on how model generates responses
    st.write(response)

# Optionally, add features like like buttons, etc.
