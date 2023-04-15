import json
import time
from .classes import Interaction
import aiohttp
from .utils import convert_to_string, URLS


async def asyncRequest(url, data, headers):
    response = None
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=json.dumps(data), headers=headers) as resp:
                response = resp
                carter_data = await response.json()
                return {"url": response.url, "carter_data": carter_data, "status_code": response.status, "status_message": response.reason, "ok": response.ok}

    except (aiohttp.ClientError, json.JSONDecodeError) as e:
        return None


class AsyncCarter:
    def __init__(self, api_key):
        self.api_key = api_key
        self.history = []

    async def say(self, text, player_id):
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
        response = await asyncRequest(URLS["say"], data, headersList)
        time_taken = int((time.perf_counter() - start) * 1000)
        interaction = Interaction("say", data, response, time_taken)
        if interaction.ok:
            self.history.insert(0, interaction)
        return interaction

    async def opener(self, player_id):
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
        response = await asyncRequest(URLS["opener"], data, headersList)
        time_taken = int((time.perf_counter() - start) * 1000)
        interaction = Interaction("opener", data, response, time_taken)
        if interaction.ok:
            self.history.insert(0, interaction)
        return interaction

    async def personalise(self, text):
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
        response = await asyncRequest(URLS["personalise"], data, headersList)
        time_taken = int((time.perf_counter() - start) * 1000)
        interaction = Interaction("personalise", data, response, time_taken)
        return interaction
