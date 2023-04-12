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
    def test_personalise_success(self):
        # Mock API response
        responses.add(
            responses.POST,
            URLS["personalise"],
            json={
                "content": "Hello, I am Carter!",
            },
            status=200
        )

        text = "Hi Carter!"

        interaction = self.carter.personalise(text)

        self.assertTrue(interaction.ok)
        self.assertEqual(interaction.status_code, 200)
        self.assertEqual(interaction.input_text, text)
        self.assertEqual(interaction.output_text, 'Hello, I am Carter!')

    def test_personalise_invalid_text(self):
      invalid_text = NonStringConvertible()

      with self.assertRaises(TypeError):
          interaction = self.carter.personalise(invalid_text)

    @responses.activate
    def test_personalise_api_error(self):
        # Mock API response
        responses.add(
            responses.POST,
            URLS["personalise"],
            json={
                "error": {
                    "message": "Forbidden",
                },
            },
            status=403
        )

        text = "Hi Carter!"

        interaction = self.carter.personalise(text)

        self.assertFalse(interaction.ok)
        self.assertEqual(interaction.status_code, 403)
        self.assertEqual(interaction.status_message, "Forbidden")

if __name__ == '__main__':
    unittest.main()
