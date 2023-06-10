# tests/test_carter.py
import os
import unittest
from dotenv import load_dotenv
from carterpy.carter import Carter, URLS
import responses
from helpers import NonStringConvertible
from testing_utils import say_payload, opener_payload, personalise_payload

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
            json=opener_payload,
            status=200
        )

        user_id = "success"

        interaction = self.carter.opener(user_id)

        self.assertTrue(interaction.ok)
        self.assertEqual(interaction.status_code, 200)
        self.assertEqual(interaction.output_text, 'RESPONSE FROM OPENER')

    def test_opener_invalid_user_id(self):
        invalid_user_id = NonStringConvertible()

        with self.assertRaises(TypeError):
            self.carter.opener(invalid_user_id)

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

        user_id = "api_error"

        interaction = self.carter.opener(user_id)

        self.assertFalse(interaction.ok)
        self.assertEqual(interaction.status_code, 403)
        self.assertEqual(interaction.status_message, "Forbidden")


if __name__ == '__main__':
    unittest.main()
