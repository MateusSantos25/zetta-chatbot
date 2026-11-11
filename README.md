# ZETTA - Chatbot com Rosto e Voz

O ZETTA e um chatbot com identidade propria, com rosto animado que pisca e voz que fala as respostas em portugues.
Ele nunca se apresenta como Google, Bard ou Gemini. Ele e o ZETTA.

## Teste Online

Acesse para testar sem instalar nada:

[ Clique aqui para testar o ZETTA ](https://zetta-chatbot.streamlit.app/)

## Funcionalidades

- Rosto proprio: Rosto animado que pisca a cada 4 segundos
- Voz: Le a resposta em voz alta em pt-BR, direto no navegador
- Memoria da conversa: Utiliza a memoria do Streamlit
- Interface estilo WhatsApp: Mensagem do usuario na direita em azul, do ZETTA na esquerda
- Identidade propria: Se perguntarem, ele responde: "Eu sou o ZETTA!"

## Como funciona

- Modelo: Gemini 3.5 Flash Lite
- Conexao: API do Google no formato OpenAI
- Interface: Streamlit
- Voz: SpeechSynthesis do navegador

## Tecnologias

- Python
- Streamlit
- OpenAI (para conectar no Gemini)

## Como rodar

```bash
pip install -r requirements.txt
streamlit run app.py