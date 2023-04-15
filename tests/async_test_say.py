# tests/test_carter.py
import asynctest
import os
import unittest
from dotenv import load_dotenv
from carterpy.async_carter import AsyncCarter, URLS
from aioresponses import aioresponses
from helpers import NonStringConvertible
load_dotenv()


class TestAsyncCarter(asynctest.TestCase):

    def setUp(self):
        self.api_key = os.getenv("CARTER_API_KEY")
        self.carter = AsyncCarter(self.api_key)

    async def test_say_success_async(self):
        # Mock API response
        with aioresponses() as mocked:
            mocked.add(
                URLS["say"],
                method="POST",
                status=200,
                payload={
                    "output": {
                        "text": "RESPONSE FROM CHARACTER",
                        "audio": "AUDIO ID"
                    },
                    "input": "INPUT MESSAGE RECEIVED",
                    "forced_behaviours": [
                        {
                            "name": "NAME OF BEHAVIOUR"
                        }
                    ]
                }
            )

            text = "Hi Carter!"
            player_id = "1234"

            interaction = await self.carter.say(text, player_id)

            self.assertTrue(interaction.ok)
            self.assertEqual(interaction.status_code, 200)
            self.assertEqual(interaction.input_text, text)
            self.assertEqual(interaction.output_text,'RESPONSE FROM CHARACTER')
            self.assertEqual(interaction.output_audio, 'AUDIO ID')

    async def test_say_invalid_text_async(self):
        invalid_text = NonStringConvertible()
        player_id = "1234"

        with self.assertRaises(TypeError) as context:
            await self.carter.say(invalid_text, player_id)

    async def test_say_invalid_player_id_async(self):
        text = "Hi Carter!"
        invalid_player_id = NonStringConvertible()

        with self.assertRaises(TypeError):
            await self.carter.say(text, invalid_player_id)

    async def test_say_api_error_async(self):
        # Mock API response
        with aioresponses() as mocked:
            mocked.add(
                URLS["say"],
                method="POST",
                status=403,
                reason="Forbidden"
            )

        text = "Hi Carter!"
        player_id = "1234"

        interaction = await self.carter.say(text, player_id)

        self.assertFalse(interaction.ok)
        self.assertEqual(interaction.status_code, 403)
        self.assertEqual(interaction.status_message, "Forbidden")


if __name__ == '__main__':
    asynctest.main()
