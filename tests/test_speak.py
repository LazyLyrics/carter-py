import os
import unittest
from carterpy.carter import Carter
from dotenv import load_dotenv
import responses
from carterpy.utils import URLS
from testing_utils import say_payload, opener_payload, personalise_payload

load_dotenv()

class TestSpeakParameter(unittest.TestCase):

    def setUp(self):
        self.api_key = os.getenv("CARTER_API_KEY")
        self.carter = Carter(self.api_key)
        self.silent_carter = Carter(self.api_key, speak=False)

    @responses.activate
    def test_say_speak_true_on_init(self):
        # Mock API responses
        responses.add(
            responses.POST,
            URLS["say"],
            json=say_payload,
            status=200
        )

        text = "This is a test message."
        user_id = "1234"
        carter = Carter(self.api_key, speak=True)

        # Test when speak is not provided
        interaction = carter.say(text, user_id)
        self.assertTrue(interaction.payload["speak"])

        # Test when speak is overridden
        interaction = carter.say(text, user_id, speak=False)
        self.assertFalse(interaction.payload["speak"])

    @responses.activate
    def test_say_speak_false_on_init(self):
        # Mock API responses
        responses.add(
            responses.POST,
            URLS["say"],
            json=say_payload,
            status=200
        )

        text = "This is a test message."
        user_id = "1234"
        carter = Carter(self.api_key, speak=False)

        # Test when speak is not provided
        interaction = carter.say(text, user_id)
        self.assertFalse(interaction.payload["speak"])

        # Test when speak is overridden
        interaction = carter.say(text, user_id, speak=True)
        self.assertTrue(interaction.payload["speak"])

    @responses.activate
    def test_say_speak_default_on_init(self):
        # Mock API responses
        responses.add(
            responses.POST,
            URLS["say"],
            json=say_payload,
            status=200
        )

        text = "This is a test message."
        user_id = "1234"
        carter = Carter(self.api_key)

        # Test when speak is not provided
        interaction = carter.say(text, user_id)
        self.assertFalse(interaction.payload["speak"])

        # Test when speak is overridden
        interaction = carter.say(text, user_id, speak=True)
        self.assertTrue(interaction.payload["speak"])

    @responses.activate
    def test_opener_speak_true_on_init(self):
        # Mock API responses
        responses.add(
            responses.POST,
            URLS["opener"],
            json=opener_payload,
            status=200
        )

        user_id = "1234"
        carter = Carter(self.api_key, speak=True)

        # Test when speak is not provided
        interaction = carter.opener(user_id)
        self.assertTrue(interaction.payload["speak"])

        # Test when speak is overridden
        interaction = carter.opener(user_id, speak=False)
        self.assertFalse(interaction.payload["speak"])

    @responses.activate
    def test_opener_speak_false_on_init(self):
        # Mock API responses
        responses.add(
            responses.POST,
            URLS["opener"],
            json=opener_payload,
            status=200
        )

        user_id = "1234"
        carter = Carter(self.api_key, speak=False)

        # Test when speak is not provided
        interaction = carter.opener(user_id)
        self.assertFalse(interaction.payload["speak"])

        # Test when speak is overridden
        interaction = carter.opener(user_id, speak=True)
        self.assertTrue(interaction.payload["speak"])

    @responses.activate
    def test_opener_speak_default_on_init(self):
        # Mock API responses
        responses.add(
            responses.POST,
            URLS["opener"],
            json=opener_payload,
            status=200
        )

        user_id = "1234"
        carter = Carter(self.api_key)

        # Test when speak is not provided
        interaction = carter.opener(user_id)
        self.assertFalse(interaction.payload["speak"])

        # Test when speak is overridden
        interaction = carter.opener(user_id, speak=True)
        self.assertTrue(interaction.payload["speak"])

    @responses.activate
    def test_personalise_speak_true_on_init(self):
        # Mock API responses
        responses.add(
            responses.POST,
            URLS["personalise"],
            json=personalise_payload,
            status=200
        )

        text = "This is a test message."
        carter = Carter(self.api_key, speak=True)

        # Test when speak is not provided
        interaction = carter.personalise(text, "user_id")
        self.assertTrue(interaction.payload["speak"])

        # Test when speak is overridden
        interaction = carter.personalise(text, "user_id", speak=False)
        self.assertFalse(interaction.payload["speak"])

    @responses.activate
    def test_personalise_speak_false_on_init(self):
        # Mock API responses
        responses.add(
            responses.POST,
            URLS["personalise"],
            json=personalise_payload,
            status=200
        )

        text = "This is a test message."
        carter = Carter(self.api_key, speak=False)

        # Test when speak is not provided
        interaction = carter.personalise(text, "user_id")
        self.assertFalse(interaction.payload["speak"])

        # Test when speak is overridden
        interaction = carter.personalise(text, "user_id", speak=True)
        self.assertTrue(interaction.payload["speak"])

    @responses.activate
    def test_personalise_speak_default_on_init(self):
        # Mock API responses
        responses.add(
            responses.POST,
            URLS["personalise"],
            json=personalise_payload,
            status=200
        )

        text = "This is a test message."
        carter = Carter(self.api_key)

        # Test when speak is not provided
        interaction = carter.personalise(text, "user_id")
        self.assertFalse(interaction.payload["speak"])

        # Test when speak is overridden
        interaction = carter.personalise(text, "user_id", speak=True)
        self.assertTrue(interaction.payload["speak"])




if __name__ == "__main__":
    unittest.main()
