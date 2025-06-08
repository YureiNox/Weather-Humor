import ollama
import os
import sys

model = "llama3.2" # Remplacez par le nom de votre modèle Ollama
system_prompt = (
    "Tu es maintenant un opérateur météo humoriste. "
    "Nous allons te donner des données météorologiques, et tu dois répondre "
    "avec une blague ou une remarque humoristique en rapport avec la météo."
    "Mais attention, tu ne dois répondre qu'avec une blague ou un poeme, tout en évitant les chose qui n'on rien à voir."
    "Fais en sorte que toute les données météorologiques soient utilisées dans ta réponse, "
)

def prompt(input_text):
    try:
        response = ollama.chat(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": input_text}
            ],
        )
        return response['message']['content']
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        return None
