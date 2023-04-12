import requests
import json
import time
from .classes import Interaction

URLS = {
    "say": "https://api.carterlabs.ai/chat",
}


class Carter:
    def __init__(self, api_key):
        self.api_key = api_key

    def say(self, text, player_id):
        try:
            text = str(text)
        except:
            raise TypeError("text must be convertible to a string")
        try:
            player_id = str(player_id)
        except:
            raise TypeError("player_id must be convertible to a string")
        start = time.perf_counter()
        data = {
            "text": text,
            "playerId": player_id,
            "key": self.api_key,
        }
        response = requests.post(URLS["say"], headers={"Content-Type": "application/json"}, data=json.dumps(data))
        time_taken = int((time.perf_counter() - start) * 1000)
        interaction = Interaction(data, response, time_taken)
        return interaction
