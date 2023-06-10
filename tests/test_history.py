# tests/test_carter.py
import os
import unittest
from dotenv import load_dotenv
from carterpy.carter import Carter, URLS
import responses
from testing_utils import say_payload, opener_payload, personalise_payload
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
            json=say_payload,
            status=200
        )

        text = "Hi Carter!"
        user_id = "1234"

        # Check that the history is initially empty
        self.assertEqual(len(self.carter.history), 0)

        # Perform a successful say interaction
        interaction = self.carter.say(text, user_id)

        # Check that the history contains one interaction
        self.assertEqual(len(self.carter.history), 1)
        self.assertEqual(interaction, self.carter.history[0])

    @responses.activate
    def test_history_after_successful_opener(self):
        # Mock API response
        responses.add(
            responses.POST,
            URLS["opener"],
            json=opener_payload,
            status=200
        )

        user_id = "history_success"

        # Check that the history is initially empty
        self.assertEqual(len(self.carter.history), 0)

        # Perform a successful opener interaction
        interaction = self.carter.opener(user_id)

        # Check that the history contains one interaction
        self.assertEqual(len(self.carter.history), 1)
        self.assertEqual(interaction, self.carter.history[0])

    @responses.activate
    def test_history_after_successful_personalise(self):
        # Mock API response
        responses.add(
            responses.POST,
            URLS["personalise"],
            json=personalise_payload,
            status=200
        )

        text = "Please personalize this text."

        # Check that the history is initially empty
        self.assertEqual(len(self.carter.history), 0)

        # Perform a successful personalise interaction
        interaction = self.carter.personalise(text, "1234")

        # Check that the history contains no interaction
        self.assertEqual(len(self.carter.history), 0)

    @responses.activate
    def test_history_after_unsuccessful_say(self):
        # Mock API response
        responses.add(
            responses.POST,
            URLS["say"],
            json={"error": "An error occurred."},
            status=403
        )

        text = "Hi Carter!"
        user_id = "1234"

        # Check that the history is initially empty
        self.assertEqual(len(self.carter.history), 0)

        # Perform an unsuccessful say interaction
        interaction = self.carter.say(text, user_id)

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

        user_id = "history_fail"

        # Check that the history is initially empty
        self.assertEqual(len(self.carter.history), 0)

        # Perform an unsuccessful opener interaction
        interaction = self.carter.opener(user_id)

        # Check that the history is still empty
        self.assertEqual(len(self.carter.history), 0)


if __name__ == '__main__':
    unittest.main()
