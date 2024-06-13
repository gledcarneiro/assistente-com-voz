# Assistente com Voz\n\n## Descrição\n\nEste projeto cria um assistente de voz interativo usando Google Cloud Speech-to-Text, GPT-4 e Google Text-to-Speech.\n\n## Configuração\n\n1. Instale as bibliotecas necessárias:\n   ```sh\n   pip install openai google-cloud-speech google-auth google-auth-oauthlib google-auth-httplib2 gtts\n   ```\n\n2. Configure as credenciais do Google Cloud:\n   - Configure um projeto no [Google Cloud Console](https://console.cloud.google.com/).\n   - Ative a API Speech-to-Text e crie credenciais (chave JSON).\n   - Baixe o arquivo de credenciais JSON e salve em `assistente_com_voz/credentials/google_credentials.json`.\n\n3. Configure a variável de ambiente:\n   ```sh\n   export GOOGLE_APPLICATION_CREDENTIALS="assistente_com_voz/credentials/google_credentials.json"\n   ```\n\n## Uso\n\n1. Execute o assistente:\n   ```sh\n   python main.py\n   ```\n\n## Estrutura do Projeto\n\n```plaintext\nassistente_com_voz/\n│\n├── credentials/\n│   └── google_credentials.json  # Credenciais do Google Cloud\n│\n├── scripts/\n│   ├── record_audio.sh          # Script para gravação de áudio\n│   ├── transcribe_audio.py      # Script para transcrição de áudio\n│   ├── gpt_response.py          # Script para obter resposta do GPT-4\n│   └── tts_response.sh          # Script para converter resposta em áudio\n│\n├── main.py                      # Script principal para executar o assistente\n│\n└── README.md                    # Instruções detalhadas do projeto\n```
