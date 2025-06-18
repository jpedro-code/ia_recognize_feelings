# 🧠 Analisador de Sentimentos com IA Gemini

Este é um projeto simples e interativo desenvolvido com **Streamlit** que utiliza a API **Gemini (Google Generative AI)** para classificar o sentimento de um texto como **Positivo**, **Negativo** ou **Neutro**.  

---

## ✨ Funcionalidades

- Análise de sentimentos baseada em IA generativa.
- Interface web simples e responsiva com Streamlit.
- Integração com os modelos mais recentes da API Gemini.
- Suporte ao carregamento de chave via `.env`.

---

## 🚀 Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/analisador-sentimentos-gemini.git
cd analisador-sentimentos-gemini
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

Ou manualmente:

```bash
pip install streamlit python-dotenv google-generativeai
```

### 3. Configure sua chave da API Gemini

1. Acesse [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)
2. Copie sua chave de API
3. Crie um arquivo chamado `.env` na raiz do projeto e adicione:

```env
GEMINI_API_KEY=coloque_sua_chave_aqui
```

### 4. Execute a aplicação

```bash
streamlit run IA.py
```

---

## 🧪 Testar outros modelos

Você pode listar todos os modelos disponíveis com o script:

```bash
python list_models.py
```

E trocar a linha abaixo no `IA.py` para o modelo desejado:

```python
model = genai.GenerativeModel("models/gemini-1.5-pro")
```

Modelos alternativos recomendados:
- `models/gemini-1.5-pro-latest`
- `models/gemini-1.5-flash`
- `models/gemini-2.5-pro` *(requer uso pago)*

---

## 📝 Exemplo de uso

Digite ou cole um texto como:

> "Estou muito feliz com o atendimento recebido hoje!"

E a IA retornará:

> **Positivo** – O texto expressa satisfação e felicidade com a experiência.

---

## 🛡️ Limitações

- A cota gratuita da API tem limites diários e por minuto.
- É necessário ativar o faturamento para usos em produção ou maiores volumes.

---

## 📄 Licença

Este projeto está sob a licença [MIT](LICENSE).

---

## 🙋‍♂️ Autores 

**João Pedro Rodrigues**  

**Haroldo Monteiro** 

**Ítalo Antônio** 
