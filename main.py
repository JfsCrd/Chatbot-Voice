import openai
import os
import speech_recognition as sr
from gtts import gTTS

# Importar as configurações da aplicação
from dotenv import load_dotenv

# Carregar a chave da API
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Definir o modelo do charbot
model = "text-davinci-002"

# Inicializar o histórico do chat
chat_historic = []

# Definir o reconhecedor de fala
r = sr.Recognizer()

# Definir o limite de energia do SR para caputra de som
sr.dynamic_energy_threshold = False

# Definir o microfone como fonte de áudio
with sr.Microphone() as source:
    # Ajustar o nível de ruído de fundo
    r.adjust_for_ambient_noise(source)

    user_input = '0'

    # Loop do chatbot
    while user_input!='sair':
        try:
            # Capturar a fala do usuário por até 5 segundos
            print("Fale alguma coisa...")
            audio = r.listen(source,)

            print('processando fala...\n')
            
            # Transcrever a fala em texto usando o reconhecedor de fala
            user_input = r.recognize_google(audio, language="pt-BR")
            chat_historic.append(f"Você: {user_input}")
           
            print('Gerando resposta...')

            # Obter a resposta do modelo do GPT-3
            response = openai.Completion.create(
                engine=model,
                # Pergunta
                prompt='\n'.join(chat_historic),
                # Controle de criativade (1 - mais criativo | 0 - nada criativo)
                temperature=0.8,
                # Tamanho da resposta (0 = indefinido)
                max_tokens=60,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )

            # Obter a resposta do modelo do GPT-3
            model_response = response.choices[0].text.strip()
            chat_historic.append(model_response)

            # Cria um objeto de áudio a partir do texto
            tts = gTTS(model_response, lang='pt-br')
            # Salva o arquivo de áudio da resposta
            tts.save("model_response.mp3")
            # Reproduz o arquivo de áudio
            os.system("start model_response.mp3")


        except sr.WaitTimeoutError:
            # Se não houver som por 2 segundos, avisar o usuário e reiniciar o loop
            print("Você não falou nada por 2 segundos. Fale novamente.")
            continue
        except sr.UnknownValueError:
            # Se não for possível transcrever a fala do usuário, avisar o usuário e reiniciar o loop
            print("Fala incompreensível. Fale novamente.")
            continue
