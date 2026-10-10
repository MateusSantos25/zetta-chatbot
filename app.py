import streamlit as st
from openai import OpenAI
import streamlit.components.v1 as components

modelo = 'gemini-3.5-flash-lite' # '3.5-flash-lite mais rapido que o 3.8'

instrucao_zetta = 'Seu nome é ZETTA. Você nunca é o google Assistant, Bard, Gemini. Se perguntarem seu nome, diga: eu sou o ZETTA!'

modelo_ia = OpenAI(api_key=st.secrets['GOOGLE_API_KEY'],
                 base_url='https://generativelanguage.googleapis.com/v1beta/openai')



def aplicar_estilo_baloes():
    st.markdown("""
    <style>
        /* Mensagem do usuário vai pra direita */
        [data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) {
            flex-direction: row-reverse;
            background-color: rgba(0, 123, 255, 1);
            margin-left: 30%;
            border-radius: 15px 15px 0px 15px;
        }
        /* Mensagem do bot fica na esquerda */
        [data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarAssistant"]) {
            background-color:  rgba(173, 216, 230, 1);
            margin-right: 30%;
            border-radius: 15px 15px 15px 0px;
        }
    </style>
    """, unsafe_allow_html=True)



def mostrar_rosto():
    html = """
    <style>
        @keyframes pisca {
            0%, 90%, 100% { height: 30px; }
            92%, 96% { height: 2px; }
        }
    </style>
    <div style="display:flex; justify-content:center;">
        <div style="width:160px; height:160px; background:#222; border:5px solid #00f2ff;
                    border-radius:40px; box-shadow: 0 0 20px #00f2ff;
                    display:flex; flex-direction:column; align-items:center; justify-content:center; gap:15px;">
            
            <div style="display:flex; gap:20px;">
                <div style="width:30px; height:30px; background:white; border-radius:50%; animation: pisca 4s infinite;"></div>
                <div style="width:30px; height:30px; background:white; border-radius:50%; animation: pisca 4s infinite;"></div>
            </div>

            <div style="width:60px; height:8px; background:#ff3b3b; border-radius:20px;"></div>
        </div>
    </div>
    """
    components.html(html, height=220)



def falar(texto):
    if len(texto) > 2000:
        texto_fala = texto[:1900] + "... resposta completa na tela."
    else:
        texto_fala = texto
    
    # limpa o texto pra não quebrar o JS
    texto_js = "".join(c for c in texto_fala if c.isalnum() or c in " ,.?!-").replace("\n"," ")
    
    # Fala no navegador sem precisar de mp3
    components.html(f"""
        <script>
        var msg = new SpeechSynthesisUtterance('{texto_js}');
        msg.lang = 'pt-BR';
        msg.rate = 1.1;
        window.speechSynthesis.cancel();
        window.speechSynthesis.speak(msg);
        </script>
    """, height=0)



def perguntar_ia(historico):
    mensagens_api = [{'role': 'system', 'content': instrucao_zetta}] + historico
    resposta_modelo = modelo_ia.chat.completions.create(
        messages=mensagens_api,
        model= modelo    
    )
    return resposta_modelo.choices[0].message.content



aplicar_estilo_baloes()

st.write('## CHATBOT ZETTA')

mostrar_rosto()

# session_state = é a memoria do strealit  
if not 'lista_mensagens' in st.session_state:
    st.session_state['lista_mensagens'] = []

# historico de mensagens 
for mensagem in st.session_state['lista_mensagens']:
    role = mensagem['role']
    content = mensagem['content']
    st.chat_message(role).write(content)

mensagem_usuario = st.chat_input('Escreva sua mensagem aqui')

if mensagem_usuario:
    st.chat_message('user').write(mensagem_usuario)
    mensagem = {'role': 'user', 'content': mensagem_usuario}
    st.session_state['lista_mensagens'].append(mensagem)

    #  resposta da Ia
    try:
        with st.spinner('ZETTA pensando...'):
            resposta_ia = perguntar_ia(st.session_state['lista_mensagens'])

    except Exception:
        st.session_state['lista_mensagens'].pop()
        st.chat_message('assistant').write('Erro de conexão ou sistema!')
        st.stop()

    # exibir a resposta da IA na tela 
    st.chat_message('assistant').write(resposta_ia)
    mensagem_ia = {'role': 'assistant', 'content':resposta_ia}
    st.session_state['lista_mensagens'].append(mensagem_ia)

# FALA - sem criar rosto novo
    falar(resposta_ia)

