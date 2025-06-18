import google.generativeai as genai
import os
from dotenv import load_dotenv

# Carrega a chave da API do .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Lista os modelos disponíveis
models = genai.list_models()

print("Modelos disponíveis:")
for model in models:
    print(f"- {model.name}")

