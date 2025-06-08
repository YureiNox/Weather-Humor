# 🌤️ **Weather Humor API** 🌤️

Bienvenue dans le projet **Weather Humor API**, une application amusante qui génère des blagues sur la météo ! 🌧️⛅

Ce projet utilise **Flask**, **OpenWeatherMap API** pour obtenir les données météorologiques, et **Ollama AI** pour générer des blagues humoristiques. Vous entrez une ville, et l'API vous répond avec une blague sur la météo. C'est simple, mais drôle ! 😄

---

## 📝 **Table des matières** 📚

1. [💡 Description du projet](#description-du-projet)
2. [⚙️ Prérequis](#prérequis)
3. [📂 Structure du projet](#structure-du-projet)
4. [🔧 Installation](#installation)
5. [🚀 Utilisation](#utilisation)
6. [🔐 Sécurité et bonnes pratiques](#sécurité-et-bonnes-pratiques)
7. [👥 Contributeurs](#contributeurs)

---

## 💡 **Description du projet**

Ce projet est une API **Flask** qui offre des blagues météo générées à partir des conditions climatiques réelles d'une ville via l'API **OpenWeatherMap** et un modèle d'IA d'**Ollama**.

### Fonctionnement général :
- **Main.py** : Demande à l'utilisateur de saisir une ville, envoie la ville au serveur Flask et attend une blague humoristique.
- **OpenWeatherMap.py** : Récupère les données météorologiques en temps réel à partir de l'API **OpenWeatherMap**.
- **generate_input.py** : Prépare l'entrée pour le modèle humoristique.
- **prompt.py** : Envoie la demande au modèle **Ollama** pour générer une réponse humoristique basée sur les données météo.
- **Server.py** : Le serveur principal Flask qui gère les requêtes et la logique des blagues météo.

---

## ⚙️ **Prérequis**

Avant de commencer, assurez-vous que vous avez installé les éléments suivants :

- **Python 3.x** (recommandé 3.7 ou supérieur) 🐍
- **Pip** pour installer les dépendances 📦

Les bibliothèques utilisées dans ce projet sont :

- `requests` 📡 : Pour les appels API externes.
- `flask` 🖥️ : Pour le serveur web.
- `ollama` 🤖 : Pour générer les blagues via le modèle d'IA.
- `threading` 🔄 : Pour gérer les tâches en arrière-plan.

---

## 📂 **Structure du projet**

Voici la structure des fichiers du projet :

```
Weather-Humor-API/
│
├── Main.py                # Point d'entrée pour l'utilisateur.
├── bin/
|   ├── __init__.py        # option non obligatoire...
│   ├── generate_input.py  # Gère la création des données pour le modèle.
│   ├── OpenWeatherMap.py  # Récupère les données météo via OpenWeatherMap.
│   ├── prompt.py          # Interagit avec le modèle Ollama.
│   └── server.py          # Serveur Flask qui gère les requêtes.
└── requirements.txt       # Liste des dépendances à installer.
```

---

## 🔧 **Installation**

### 1. Clonez le dépôt

```
git clone https://github.com/yureinox/Weather-Humor.git
cd weather-humor-api
```

### 2. Créez un environnement virtuel

Créez un environnement virtuel pour isoler les dépendances du projet :

```
python -m venv venv
source venv/bin/activate  # Sur Windows, utilisez `venv\Scripts\activate`
```

### 3. Installez les dépendances

Installez toutes les dépendances nécessaires :

```
pip install -r requirements.txt
```

### 4. Configurez l'API OpenWeatherMap

- Obtenez une clé API sur [OpenWeatherMap](https://openweathermap.org/) 🗝️.
- Remplacez `"YOUR_API_KEY_HERE"` par votre clé API dans `OpenWeatherMap.py`.

### 5. Installez Ollama AI

Assurez-vous que le modèle **Ollama** est installé et accessible depuis votre script Python.

---

## 🚀 **Utilisation**

### Démarrer le serveur Flask

Lancez le serveur Flask pour démarrer l'API :

```
python bin/server.py
```

Le serveur sera accessible à l'adresse `http://127.0.0.1:5000` 🌍.

### Utilisation de l'application

1. **Main.py** : Lancez le fichier `Main.py` pour commencer à interagir avec l'application :

```
python Main.py
```

Vous serez invité à entrer le nom d'une ville. Après l'envoi, l'application attendra la réponse de l'API et vous fournira une blague météo générée par l'IA 🤖.

2. **Points d'API** :
   - `POST /api/weather/send_city` 🌆 : Envoie une ville pour récupérer les données météo.
   - `GET /api/weather/wait` ⏳ : Attendre la blague générée par le modèle.

---

## 🔐 **Sécurité et bonnes pratiques**

### 1. **Clé API sécurisée** 🔑
**Ne jamais exposer votre clé API publiquement !** Utilisez des variables d'environnement ou un fichier de configuration non suivi par Git.

Exemple avec des variables d'environnement :

```
export OPENWEATHER_API_KEY="votre_clé_api"
```

Dans `OpenWeatherMap.py` :

```
import os
api_key = os.getenv('OPENWEATHER_API_KEY')
```

### 2. **Limiter l'accès à l'API** ⚖️
Respectez les limites d'utilisation de l'API **OpenWeatherMap** pour éviter toute suspension de service. Consultez la [documentation de l'API](https://openweathermap.org/api).

### 3. **Sécuriser Flask pour la production** 🛡️
Le serveur **Flask** utilisé ici est un serveur de développement. Pour un environnement de production, assurez-vous de sécuriser l'API avec HTTPS et des mécanismes d'authentification.

---

🌟 Merci d'utiliser **Weather Humor API** 🌟  
Nous espérons que vous allez rigoler avec vos nouvelles blagues météo ! 😆

