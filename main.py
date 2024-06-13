import os\n\n# Gravar áudio de entrada\nos.system("bash scripts/record_audio.sh")\n\n# Transcrever áudio\nos.system("python scripts/transcribe_audio.py > transcribed_question.txt")\nwith open("transcribed_question.txt", "r") as file:\n    question = file.read().strip()\n\n# Obter resposta do GPT-4\nos.system(f"python scripts/gpt_response.py \"{question}\" > gpt_response.txt")\nwith open("gpt_response.txt", "r") as file:\n    answer = file.read().strip()\n\n# Converter resposta em áudio\nos.system(f"bash scripts/tts_response.sh \"{answer}\"")
