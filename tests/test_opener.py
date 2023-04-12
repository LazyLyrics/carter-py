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
    def test_opener_success(self):
      # Mock API response
      responses.add(
          responses.POST,
          URLS["opener"],
          json={
              "sentence": "Hello, I am Carter!",
          },
          status=200
      )

      player_id = "1234"

      interaction = self.carter.opener(player_id)

      self.assertTrue(interaction.ok)
      self.assertEqual(interaction.status_code, 200)
      self.assertEqual(interaction.output_text, 'Hello, I am Carter!')

    def test_opener_invalid_player_id(self):
        invalid_player_id = NonStringConvertible()

        with self.assertRaises(TypeError):
            self.carter.opener(invalid_player_id)

    @responses.activate
    def test_opener_api_error(self):
      # Mock API response
      responses.add(
          responses.POST,
          URLS["opener"],
          json={
              "error": {
                  "message": "Invalid API key",
              },
          },
          status=403
      )

      player_id = "1234"

      interaction = self.carter.opener(player_id)

      self.assertFalse(interaction.ok)
      self.assertEqual(interaction.status_code, 403)
      self.assertEqual(interaction.status_message, "Forbidden")

if __name__ == '__main__':
    unittest.main()
