# generate_input.py
weather_data = None  # Ceci sera rempli par server.py

def generate_input():
    """
    Generate input data for the weather humor model.
    """
    input_text = f"Voici les données météorologiques actuelles : {weather_data}. Quelle est ta blague ou remarque humoristique ?"
    return input_text
