# ZETTA 🤖 - Chatbot com Rosto e Voz

O ZETTA é um chatbot com identidade própria, com rosto animado que pisca e voz que fala as respostas em português.
Ele nunca se apresenta como Google, Bard ou Gemini. Ele é o ZETTA!

## 🚀 Teste Online Agora

👉 [Clique aqui para testar o ZETTA](https://zetta-chatbot.streamlit.app/)

## ✨ O que ele faz

- **Tem rosto próprio:** Rosto animado que pisca a cada 4 segundos
- **Fala de verdade:** Lê a resposta em voz alta em pt-BR, direto no navegador
- **Lembra da conversa:** Usa a memória do Streamlit
- **Visual estilo WhatsApp:** Sua mensagem na direita em azul, a do ZETTA na esquerda
- **Identidade própria:** Se perguntarem, ele responde: "Eu sou o ZETTA!"

## 🧠 Como ele funciona

- **Modelo:** Gemini 3.5 Flash Lite
- **Conexão:** API do Google no formato OpenAI
- **Interface:** Streamlit
- **Voz:** SpeechSynthesis do navegador

## 🛠️ Tecnologias

- Python
- Streamlit
- OpenAI (para conectar no Gemini)

## 💻 Como rodar

```bash
pip install -r requirements.txt
streamlit run app.py