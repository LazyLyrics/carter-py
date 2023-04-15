# tests/test_carter.py
import asynctest
import os
import unittest
from dotenv import load_dotenv
from carterpy.async_carter import AsyncCarter, URLS
from aioresponses import aioresponses
from helpers import NonStringConvertible

load_dotenv()


class TestAsyncCarter(asynctest.TestCase):

    def setUp(self):
        self.api_key = os.getenv("CARTER_API_KEY")
        self.carter = AsyncCarter(self.api_key)

    async def test_personalise_success_async(self):
        # Mock API response
        with aioresponses() as mocked:
            mocked.add(
                URLS["personalise"],
                method="POST",
                status=200,
                payload={
                    "content": "Hello, I am Carter!",
                }
            )

            text = "Hi Carter!"

            interaction = await self.carter.personalise(text)

            self.assertTrue(interaction.ok)
            self.assertEqual(interaction.status_code, 200)
            self.assertEqual(interaction.input_text, text)
            self.assertEqual(interaction.output_text, 'Hello, I am Carter!')

    async def test_personalise_invalid_text_async(self):
        invalid_text = NonStringConvertible()

        with self.assertRaises(TypeError):
            interaction = await self.carter.personalise(invalid_text)

    async def test_personalise_api_error_async(self):
        # Mock API response
        with aioresponses() as mocked:
            mocked.add(
                URLS["personalise"],
                method="POST",
                status=403,
                reason="Forbidden"
            )

            text = "Hi Carter!"

            interaction = await self.carter.personalise(text)

            self.assertFalse(interaction.ok)
            self.assertEqual(interaction.status_code, 403)
            self.assertEqual(interaction.status_message, "Forbidden")


if __name__ == '__main__':
    asynctest.main()
