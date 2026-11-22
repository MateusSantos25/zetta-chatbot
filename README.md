# ZETTA: chatbot com rosto e voz

O ZETTA é um chatbot com identidade própria: tem um rosto animado que pisca e uma voz que lê as respostas em português.
Ele nunca se apresenta como Google, Bard ou Gemini. Ele é o ZETTA.

## Teste online

Acesse para testar sem instalar nada:

[Clique aqui para testar o ZETTA](https://zetta-chatbot.streamlit.app/)

## Funcionalidades

- **Rosto próprio:** rosto animado que pisca a cada 4 segundos
- **Voz:** lê a resposta em voz alta em pt-BR, direto no navegador
- **Memória da conversa:** lembra o que foi dito durante a sessão (usa o `session_state` do Streamlit)
- **Interface estilo WhatsApp:** mensagens do usuário à direita, em azul, e as do ZETTA à esquerda
- **Identidade própria:** se perguntarem o nome, ele responde "Eu sou o ZETTA!"

## Como funciona

| Parte      | Tecnologia                                         |
|------------|----------------------------------------------------|
| Modelo     | Gemini 3.5 Flash Lite                              |
| Conexão    | API do Google no formato compatível com a OpenAI   |
| Interface  | Streamlit                                          |
| Voz        | SpeechSynthesis, a API de fala do próprio navegador |

## Como rodar localmente

### Pré-requisitos

- Python (testado na versão 3.14)
- Uma chave da API do Gemini, que pode ser gerada gratuitamente no [Google AI Studio](https://aistudio.google.com/apikey)

### Passo a passo

1. Clone o repositório e entre na pasta:

   ```bash
   git clone https://github.com/MateusSantos25/zetta-chatbot.git
   cd zetta-chatbot
   ```

2. Crie e ative um ambiente virtual:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate      # Windows
   source .venv/bin/activate   # Linux/macOS
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure a chave da API. Crie o arquivo `.streamlit/secrets.toml` com o conteúdo:

   ```toml
   GOOGLE_API_KEY = "sua-chave-aqui"
   ```

   > Esse arquivo está no `.gitignore` e nunca deve ir para o repositório.

5. Rode o app:

   ```bash
   streamlit run app.py
   ```

   O navegador abre em `http://localhost:8501`.

## Limitações conhecidas

- **A memória dura só uma sessão:** ao recarregar a página, a conversa é apagada, porque ainda não existe banco de dados.
- **A voz depende do navegador:** a qualidade e o sotaque mudam conforme o navegador e o sistema, e alguns não têm voz em pt-BR.
- **Respostas longas são lidas pela metade:** acima de 2000 caracteres, o ZETTA lê só o começo e avisa que a resposta completa está na tela.
- **O app online "dorme" sem acessos:** depois de um período sem visitas, o Streamlit Cloud desliga o app para economizar recursos do servidor. Quem acessar nesse momento precisa clicar no botão para reativar e esperar alguns segundos.

## Próximos passos

- [ ] Botão para ligar e desligar o áudio
- [ ] Informar o clima
- [ ] Enviar mensagens por voz (fala convertida em texto)
- [ ] Buscar informações em tempo real
- [ ] Gerar documentos e links e fazer upload de arquivos
