# tests/test_carter.py
import asynctest
import os
import unittest
from dotenv import load_dotenv
from carterpy.async_carter import AsyncCarter, URLS
from aioresponses import aioresponses
from helpers import NonStringConvertible
from testing_utils import say_payload, opener_payload, personalise_payload

load_dotenv()


class TestAsyncCarter(asynctest.TestCase):

    def setUp(self):
        self.api_key = os.getenv("CARTER_API_KEY")
        self.carter = AsyncCarter(self.api_key)

    async def test_opener_success_async(self):
        # Mock API response
        with aioresponses() as mocked:
            mocked.add(
                URLS["opener"],
                method="POST",
                status=200,
                payload=opener_payload
            )

            user_id = "success"

            interaction = await self.carter.opener(user_id)

            self.assertTrue(interaction.ok)
            self.assertEqual(interaction.status_code, 200)
            self.assertEqual(interaction.output_text, 'RESPONSE FROM OPENER')

    async def test_opener_invalid_user_id_async(self):
        invalid_user_id = NonStringConvertible()

        with self.assertRaises(TypeError):
            await self.carter.opener(invalid_user_id)

    async def test_opener_api_error_async(self):
        # Mock API response
        with aioresponses() as mocked:
            mocked.add(
                URLS["opener"],
                method="POST",
                status=403,
                reason="Forbidden"
            )

            user_id = "api_error"

            interaction = await self.carter.opener(user_id)

            self.assertFalse(interaction.ok)
            self.assertEqual(interaction.status_code, 403)
            self.assertEqual(interaction.status_message, "Forbidden")


if __name__ == '__main__':
    asynctest.main()
