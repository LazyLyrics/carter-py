import requests
import json
import time
from .classes import Interaction
from .utils import convert_to_string, URLS


def carterRequest(url, data, headers):
    try:
        response = requests.post(
            url, data=json.dumps(data), headers=headers)
        carter_data = response.json()
        return {"carter_data": carter_data, "status_code": response.status_code, "status_message": response.reason, "ok": response.ok, "url": response.url}
    except (requests.exceptions.RequestException, json.JSONDecodeError) as e:
        return None


class Carter:
    def __init__(self, api_key):
        self.api_key = api_key
        self.history = []

    def say(self, text, player_id):
        text = convert_to_string("text", text)
        player_id = convert_to_string("player_id", player_id)
        start = time.perf_counter()
        data = {
            "text": text,
            "playerId": player_id,
            "key": self.api_key,
        }

        headersList = {
            "Accept": "*/*",
            "Content-Type": "application/json"
        }

        response = carterRequest(URLS["say"], data, headers=headersList)
        time_taken = int((time.perf_counter() - start) * 1000)
        interaction = Interaction("say", data, response, time_taken)
        if interaction.ok:
            self.history.insert(0, interaction)
        return interaction

    def opener(self, player_id):
        player_id = convert_to_string("player_id", player_id)
        start = time.perf_counter()
        data = {
            "playerId": player_id,
            "key": self.api_key,
        }
        headersList = {
            "Accept": "*/*",
            "Content-Type": "application/json"
        }
        response = carterRequest(
            URLS["opener"], headers=headersList, data=data)
        time_taken = int((time.perf_counter() - start) * 1000)
        interaction = Interaction("opener", data, response, time_taken)
        if interaction.ok:
            self.history.insert(0, interaction)
        return interaction

    def personalise(self, text):
        text = convert_to_string("text", text)
        start = time.perf_counter()
        data = {
            "text": text,
            "key": self.api_key,
        }
        headersList = {
            "Accept": "*/*",
            "Content-Type": "application/json"
        }
        response = carterRequest(
            URLS["personalise"], headers=headersList, data=data)
        time_taken = int((time.perf_counter() - start) * 1000)
        interaction = Interaction("personalise", data, response, time_taken)
        return interaction
