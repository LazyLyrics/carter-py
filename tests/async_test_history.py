# tests/test_carter.py
import asynctest
import os
import unittest
from dotenv import load_dotenv
from carterpy.async_carter import AsyncCarter, URLS
from aioresponses import aioresponses
from testing_utils import say_payload, opener_payload, personalise_payload

load_dotenv()

class TestAsyncCarter(asynctest.TestCase):

    def setUp(self):
        self.api_key = os.getenv("CARTER_API_KEY")
        self.carter = AsyncCarter(self.api_key)

    async def test_history_after_successful_say_async(self):
        # Mock API response
        with aioresponses() as mocked:
            mocked.add(
                URLS["say"],
                method="POST",
                status=200,
                payload=say_payload
            )

            text = "Hi Carter!"
            user_id = "1234"

            # Check that the history is initially empty
            self.assertEqual(len(self.carter.history), 0)

            # Perform a successful say interaction
            interaction = await self.carter.say(text, user_id)

            # Check that the history contains one interaction
            self.assertEqual(len(self.carter.history), 1)
            self.assertEqual(interaction, self.carter.history[0])

    async def test_history_after_successful_opener_async(self):
        # Mock API response
        with aioresponses() as mocked:
            mocked.add(
                URLS["opener"],
                method="POST",
                status=200,
                payload=opener_payload
            )

            user_id = "history_success"

            # Check that the history is initially empty
            self.assertEqual(len(self.carter.history), 0)

            # Perform a successful opener interaction
            interaction = await self.carter.opener(user_id)

            # Check that the history contains one interaction
            self.assertEqual(len(self.carter.history), 1)
            self.assertEqual(interaction, self.carter.history[0])

    async def test_history_after_successful_personalise_async(self):
        # Mock API response
        with aioresponses() as mocked:
            mocked.add(
                URLS["personalise"],
                method="POST",
                status=200,
                payload=personalise_payload
            )

            text = "Please personalize this text."
            user_id = "1234"

            # Check that the history is initially empty
            self.assertEqual(len(self.carter.history), 0)

            # Perform a successful personalise interaction
            interaction = await self.carter.personalise(text, user_id)

            # Check that the history contains no interaction
            self.assertEqual(len(self.carter.history), 0)


    async def test_history_after_unsuccessful_say_async(self):
        # Mock API response
        with aioresponses() as mocked:
            mocked.add(
                URLS["say"],
                method="POST",
                status=403,
                reason="Forbidden"
            )

            text = "Hi Carter!"
            user_id = "1234"

            # Check that the history is initially empty
            self.assertEqual(len(self.carter.history), 0)

            # Perform an unsuccessful say interaction
            interaction = await self.carter.say(text, user_id)

            # Check that the history is still empty
            self.assertEqual(len(self.carter.history), 0)

    async def test_history_after_unsuccessful_opener_async(self):
        # Mock API response
        with aioresponses() as mocked:
            mocked.add(
                URLS["opener"],
                method="POST",
                status=400,
                reason="Bad Request"
            )

            user_id = "history_fail"

            # Check that the history is initially empty
            self.assertEqual(len(self.carter.history), 0)

            # Perform an unsuccessful opener interaction
            interaction = await self.carter.opener(user_id)

            # Check that the history is still empty
            self.assertEqual(len(self.carter.history), 0)


if __name__ == '__main__':
    asynctest.main()
