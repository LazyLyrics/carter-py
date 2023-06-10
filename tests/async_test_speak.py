import os
import asynctest
from carterpy.async_carter import AsyncCarter
from dotenv import load_dotenv
from aioresponses import aioresponses
from carterpy.utils import URLS
from testing_utils import say_payload, opener_payload, personalise_payload

load_dotenv()

class TestSpeakParameter(asynctest.TestCase):

    def setUp(self):
        self.api_key = os.getenv("CARTER_API_KEY")
        self.carter = AsyncCarter(self.api_key)
        self.silent_carter = AsyncCarter(self.api_key, speak=False)

    async def test_say_speak_true_on_init(self):
        # Mock API responses
        with aioresponses() as mocked:
            mocked.add(
                URLS["say"],
                method="POST",
                status=200,
                payload=say_payload
            )

            text = "This is a test message."
            user_id = "1234"
            carter = AsyncCarter(self.api_key, speak=True)

            # Test when speak is not provided
            interaction = await carter.say(text, user_id)
            self.assertTrue(interaction.payload["speak"])

            # Test when speak is overridden
            interaction = await carter.say(text, user_id, speak=False)
            self.assertFalse(interaction.payload["speak"])

    async def test_say_speak_false_on_init(self):
        # Mock API responses
        with aioresponses() as mocked:
            mocked.add(
                URLS["say"],
                method="POST",
                status=200,
                payload=say_payload
            )

            text = "This is a test message."
            user_id = "1234"
            carter = AsyncCarter(self.api_key, speak=False)

            # Test when speak is not provided
            interaction = await carter.say(text, user_id)
            self.assertFalse(interaction.payload["speak"])

            # Test when speak is overridden
            interaction = await carter.say(text, user_id, speak=True)
            self.assertTrue(interaction.payload["speak"])

    async def test_say_speak_default_on_init(self):
        # Mock API responses
        with aioresponses() as mocked:
            mocked.add(
                URLS["say"],
                method="POST",
                status=200,
                payload=say_payload
            )

            text = "This is a test message."
            player_id = "1234"
            carter = AsyncCarter(self.api_key)

            # Test when speak is not provided
            interaction = await carter.say(text, player_id)
            self.assertFalse(interaction.payload["speak"])

            # Test when speak is overridden
            interaction = await carter.say(text, player_id, speak=True)
            self.assertTrue(interaction.payload["speak"])

    async def test_opener_speak_true_on_init(self):
        # Mock API responses
        with aioresponses() as mocked:
            mocked.add(
                URLS["opener"],
                method="POST",
                status=200,
                payload=opener_payload
            )

            player_id = "1234"
            carter = AsyncCarter(self.api_key, speak=True)

            # Test when speak is not provided
            interaction = await carter.opener(player_id)
            self.assertTrue(interaction.payload["speak"])

            # Test when speak is overridden
            interaction = await carter.opener(player_id, speak=False)
            self.assertFalse(interaction.payload["speak"])

    async def test_opener_speak_false_on_init(self):
        # Mock API responses
        with aioresponses() as mocked:
            mocked.add(
                URLS["opener"],
                method="POST",
                status=200,
                payload=opener_payload
            )

            player_id = "1234"
            carter = AsyncCarter(self.api_key, speak=False)

            # Test when speak is not provided
            interaction = await carter.opener(player_id)
            self.assertFalse(interaction.payload["speak"])

            # Test when speak is overridden
            interaction = await carter.opener(player_id, speak=True)
            self.assertTrue(interaction.payload["speak"])

    async def test_opener_speak_default_on_init(self):
        # Mock API responses
        with aioresponses() as mocked:
            mocked.add(
                URLS["opener"],
                method="POST",
                status=200,
                payload=opener_payload
            )

            player_id = "1234"
            carter = AsyncCarter(self.api_key)

            # Test when speak is not provided
            interaction = await carter.opener(player_id)
            self.assertFalse(interaction.payload["speak"])

            # Test when speak is overridden
            interaction = await carter.opener(player_id, speak=True)
            self.assertTrue(interaction.payload["speak"])

    async def test_personalise_speak_true_on_init(self):
        # Mock API responses
        with aioresponses() as mocked:
            mocked.add(
                URLS["personalise"],
                method="POST",
                status=200,
                payload=personalise_payload
            )

            text = "This is a test message."
            carter = AsyncCarter(self.api_key, speak=True)

            # Test when speak is not provided
            interaction = await carter.personalise(text, "user_id")
            self.assertTrue(interaction.payload["speak"])

            # Test when speak is overridden
            interaction = await carter.personalise(text, "user_id", speak=False)
            self.assertFalse(interaction.payload["speak"])

    async def test_personalise_speak_false_on_init(self):
        # Mock API responses
        with aioresponses() as mocked:
            mocked.add(
                URLS["personalise"],
                method="POST",
                status=200,
                payload=personalise_payload
            )

            text = "This is a test message."
            carter = AsyncCarter(self.api_key, speak=False)

            # Test when speak is not provided
            interaction = await carter.personalise(text, "user_id")
            self.assertFalse(interaction.payload["speak"])

            # Test when speak is overridden
            interaction = await carter.personalise(text, "user_id", speak=True)
            self.assertTrue(interaction.payload["speak"])


    async def test_personalise_speak_default_on_init(self):
        # Mock API responses
        with aioresponses() as mocked:
            mocked.add(
                URLS["personalise"],
                method="POST",
                status=200,
                payload=personalise_payload
            )

            text = "This is a test message."
            carter = AsyncCarter(self.api_key)

            # Test when speak is not provided
            interaction = await carter.personalise(text, user_id="user_id")
            self.assertFalse(interaction.payload["speak"])

            # Test when speak is overridden
            interaction = await carter.personalise(text, user_id="user_id", speak=True)
            self.assertTrue(interaction.payload["speak"])

if __name__ == '__main__':
    asynctest.main()
