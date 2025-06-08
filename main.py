import requests
import time

BASE_URL = "http://127.0.0.1:5000"
CITY = input("🌆 Entrez le nom de la ville : ")

def send_city(city):
    url = f"{BASE_URL}/api/weather/send_city"
    payload = {"city": city}
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        print("✅ Requête envoyée :", response.json()["message"])
    except requests.RequestException as e:
        print("❌ Erreur lors de l'envoi :", e)
        return False
    return True

def wait_for_response():
    url = f"{BASE_URL}/api/weather/wait"
    print("⏳ En attente de la réponse du modèle...")

    while True:
        try:
            response = requests.get(url)
            data = response.json()

            if data["status"] == "done":
                print("🎉 Réponse reçue !")
                print("💬 Blague météo :", data["joke"])
                break
            else:
                print("... toujours en attente")
                time.sleep(1)
        except requests.RequestException as e:
            print("❌ Erreur lors de la récupération :", e)
            break

if __name__ == "__main__":
    if send_city(CITY):
        wait_for_response()
