from flask import Flask, request, jsonify
from threading import Thread
import time

from OpenWeatherMap import get_weather
from generate_input import generate_input
import generate_input as input_module
from prompt import prompt

app = Flask(__name__)

# Pour stocker la réponse temporairement
response_data = {"result": None}


def background_task(weather):
    input_module.weather_data = weather
    input_text = generate_input()
    joke = prompt(input_text)
    response_data["result"] = joke


@app.route("/api/weather/send_city", methods=["POST"])
def send_city():
    data = request.get_json()
    if not data or "city" not in data:
        return jsonify({"error": "Ville non spécifiée"}), 400

    city = data["city"]
    weather = get_weather(city)

    if isinstance(weather, str) and weather.startswith("Error"):
        return jsonify({"error": weather}), 400

    # Lancer la tâche dans un thread séparé
    thread = Thread(target=background_task, args=(weather,))
    thread.start()

    return jsonify({"message": "Traitement lancé. Vérifiez /api/weather/wait pour le résultat."})


@app.route("/api/weather/wait", methods=["GET"])
def wait_for_response():
    timeout = 15  # secondes max
    waited = 0

    while response_data["result"] is None and waited < timeout:
        time.sleep(1)
        waited += 1

    if response_data["result"] is None:
        return jsonify({"status": "pending", "message": "Toujours en attente de la réponse."})

    result = response_data["result"]
    response_data["result"] = None  # reset après réponse
    return jsonify({"status": "done", "joke": result})


if __name__ == "__main__":
    app.run(debug=True)
