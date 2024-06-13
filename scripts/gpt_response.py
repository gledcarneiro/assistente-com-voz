import openai\n\nopenai.api_key = "YOUR_OPENAI_API_KEY"\n\ndef ask_gpt(question):\n    response = openai.Completion.create(\n        engine="text-davinci-004",\n        prompt=question,\n        max_tokens=150\n    )\n    return response.choices[0].text.strip()\n\nif __name__ == "__main__":\n    import sys\n    question = sys.argv[1]\n    answer = ask_gpt(question)\n    print(f"Resposta do GPT-4: {answer}")
