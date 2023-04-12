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
    def test_history_after_successful_say(self):
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

        text = "Hi Carter!"
        player_id = "1234"

        # Check that the history is initially empty
        self.assertEqual(len(self.carter.history), 0)

        # Perform a successful say interaction
        interaction = self.carter.say(text, player_id)

        # Check that the history contains one interaction
        self.assertEqual(len(self.carter.history), 1)
        self.assertEqual(interaction, self.carter.history[0])

    @responses.activate
    def test_history_after_successful_opener(self):
        # Mock API response
        responses.add(
            responses.POST,
            URLS["opener"],
            json={"sentence": "RESPONSE FROM OPENER"},
            status=200
        )

        player_id = "1234"

        # Check that the history is initially empty
        self.assertEqual(len(self.carter.history), 0)

        # Perform a successful opener interaction
        interaction = self.carter.opener(player_id)

        # Check that the history contains one interaction
        self.assertEqual(len(self.carter.history), 1)
        self.assertEqual(interaction, self.carter.history[0])

    @responses.activate
    def test_history_after_successful_personalise(self):
        # Mock API response
        responses.add(
            responses.POST,
            URLS["personalise"],
            json={"content": "RESPONSE FROM PERSONALISE"},
            status=200
        )

        text = "Please personalize this text."

        # Check that the history is initially empty
        self.assertEqual(len(self.carter.history), 0)

        # Perform a successful personalise interaction
        interaction = self.carter.personalise(text)

        # Check that the history contains no interaction
        self.assertEqual(len(self.carter.history), 0)

    @responses.activate
    def test_history_after_unsuccessful_say(self):
        # Mock API response
        responses.add(
            responses.POST,
            URLS["say"],
            json={"error": "An error occurred."},
            status=400
        )

        text = "Hi Carter!"
        player_id = "1234"

        # Check that the history is initially empty
        self.assertEqual(len(self.carter.history), 0)

        # Perform an unsuccessful say interaction
        interaction = self.carter.say(text, player_id)

        # Check that the history is still empty
        self.assertEqual(len(self.carter.history), 0)

    @responses.activate
    def test_history_after_unsuccessful_opener(self):
        # Mock API response
        responses.add(
            responses.POST,
            URLS["opener"],
            json={"error": "An error occurred."},
            status=400
        )

        player_id = "1234"

        # Check that the history is initially empty
        self.assertEqual(len(self.carter.history), 0)

        # Perform an unsuccessful opener interaction
        interaction = self.carter.opener(player_id)

        # Check that the history is still empty
        self.assertEqual(len(self.carter.history), 0)



if __name__ == '__main__':
    unittest.main()
