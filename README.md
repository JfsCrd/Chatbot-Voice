# Chatbot-Voice with ChatGPT

A populidade do chatGPT deu início à uma série de ideias que têm sido desenvolvidas no mundo todo. Pegando carona neste boom, este projeto implementa um chatbot por voz usando a API da OpenAI. Além de habilidades de programação, alguns passos gerados pelo ChatGPT foram utilizados para seu desenvolvimento.

Mesmo existindo uma série de projetos similares disponíveis no GitHub, este foi desenvolvido para reforçar o aprendizado e conhecimento pyhton, frameworks e APIs.

---
## Testando a Aplicação

### Dependências 📒
```pip install openai```
```pip install python-dotenv```
```pip install SpeechRecognition```
```pip install PyAudio```
```pip install gtts```

### Para usar 👨‍💻
- Obtenha uma API Key da OpenAI [clique aqui](https://platform.openai.com/account/api-keys);
- Crie um arquivo ```.env``` com o seguinte conteúdo:
    ```OPENAI_API_KEY=suaapikey```
- Instale as depêndencias acima, caso não as tenha instalado na máquina;

---
## Notas

### ℹ️ Sobre a versão atual ℹ️
Frequentemente o bot responde com um ponto de interrogação ('?') e este é capturado no áudio. Em uma futura atualização este caracter será escapado.

### ⚠️ ATENÇÃO ⚠️
O uso da API da OpenAi tem custos!
O plano gratuito disponibiliza $18.00 em créditos, o que cobre 9milhões de tokens no modelo Curie e 900mil tonkens no modelo Davinci (mais avançado).

Saiba mais sobre planos e preços [clicando aqui](https://openai.com/pricing)

Use por sua conta e risco.