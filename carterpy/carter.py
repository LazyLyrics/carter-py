import requests
import json
import time
from .classes import Interaction, OpenerInteraction, PersonaliseInteraction
from .utils import convert_to_string

URLS = {
    "say": "https://api.carterlabs.ai/chat",
    "opener": "https://api.carterlabs.ai/opener",
    "personalise": "https://api.carterlabs.ai/personalise",
}

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
        response = requests.post(URLS["say"], headers={"Content-Type": "application/json"}, data=json.dumps(data))
        time_taken = int((time.perf_counter() - start) * 1000)
        interaction = Interaction(data, response, time_taken)
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
        response = requests.post(URLS["opener"], headers=headersList, data=json.dumps(data))
        time_taken = int((time.perf_counter() - start) * 1000)
        interaction = OpenerInteraction(data, response, time_taken)
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
        response = requests.post(URLS["personalise"], headers=headersList, data=json.dumps(data))
        time_taken = int((time.perf_counter() - start) * 1000)
        interaction = PersonaliseInteraction(data, response, time_taken)
        return interaction
