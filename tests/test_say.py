# tests/test_carter.py
import os
import unittest
from dotenv import load_dotenv
from carterpy.carter import Carter, URLS
import responses
from helpers import NonStringConvertible
load_dotenv()


class TestCarter(unittest.TestCase):

    def setUp(self):
        self.api_key = os.getenv("CARTER_API_KEY")
        self.carter = Carter(self.api_key)

    @responses.activate
    def test_say_success(self):
        # Mock API response
        responses.add(
            responses.POST,
            URLS["say"],
            json={
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
            },
            status=200
        )

        text = "This is another test message."
        player_id = "1234"

        interaction = self.carter.say(text, player_id)

        self.assertTrue(interaction.ok)
        self.assertEqual(interaction.status_code, 200)
        self.assertEqual(interaction.input_text, text)
        self.assertEqual(interaction.output_text, 'RESPONSE FROM CHARACTER')
        self.assertEqual(interaction.output_audio, 'AUDIO ID')

    def test_say_invalid_text(self):
        invalid_text = NonStringConvertible()
        player_id = "1234"

        with self.assertRaises(TypeError) as context:
            self.carter.say(invalid_text, player_id)

    def test_say_invalid_player_id(self):
        text = "Hi Carter!"
        invalid_player_id = NonStringConvertible()

        with self.assertRaises(TypeError):
            self.carter.say(text, invalid_player_id)

    @responses.activate
    def test_say_api_error(self):
        # Mock API response
        responses.add(
            responses.POST,
            URLS["say"],
            json={
                "error": {
                    "message": "Invalid API key",
                },
            },
            status=403
        )

        text = "Hi Carter!"
        player_id = "1234"

        interaction = self.carter.say(text, player_id)

        self.assertFalse(interaction.ok)
        self.assertEqual(interaction.status_code, 403)
        self.assertEqual(interaction.status_message, "Forbidden")
        self.assertIsNone(interaction.output_text)


if __name__ == '__main__':
    unittest.main()
