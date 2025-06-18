import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Carrega a chave da API
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("Erro: API KEY não encontrada! Verifique seu arquivo .env.")
    st.stop()
# Configura Gemini
genai.configure(api_key=api_key)
model = genai.GenerativeModel('models/gemini-1.5-flash')

# Interface
st.set_page_config(page_title="Analisador de Sentimentos", layout="centered")
st.title("🧠 Analisador de Sentimentos com IA Gemini")

user_text = st.text_area("Digite ou cole um texto para análise:")

if st.button("Analisar Sentimento"):
    if not user_text.strip():
        st.warning("Digite algum texto antes de enviar.")
    else:
        with st.spinner("Analisando com IA..."):
            prompt = f"""
Classifique o sentimento do seguinte texto como Positivo, Negativo ou Neutro.
Retorne apenas a classificação e uma breve justificativa.

Texto:
\"\"\"{user_text}\"\"\"
"""
            response = model.generate_content(prompt)
            st.success("Análise concluída!")
            st.markdown(f"### Resultado da IA:\n{response.text}")
