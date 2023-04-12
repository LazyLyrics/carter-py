import unittest
from carterpy.carter import Carter
from carterpy.classes import Interaction
from dotenv import load_dotenv
load_dotenv()
import os
import logging
import sys

class TestCarter(unittest.TestCase):

    class UnconvertibleToString:
            def __str__(self):
                raise Exception("Cannot convert to string")
    def setUp(self):
        self.carter = Carter(os.environ.get("CARTER_API_KEY"))

    def test_valid_say(self):
        logger = logging.getLogger( "SomeTest.testSomething" )
        # Test valid input
        input_text = "Hello"
        player_id = "12345"
        interaction = self.carter.say(input_text, player_id)
        logger.debug(interaction)
        self.assertIsInstance(interaction, Interaction)
        self.assertEqual(interaction.input_text, input_text)
        self.assertTrue(interaction.ok)
        self.assertEqual(interaction.status_code, 200)
        self.assertEqual(interaction.status_message, "OK")
        self.assertIsNotNone(interaction.output_text)
        self.assertIsNotNone(interaction.forced_behaviours)

    def test_valid_text_unconvertible_player_id(self):
        input_text = "Hello"
        player_id = TestCarter.UnconvertibleToString()

        with self.assertRaises(TypeError):
            interaction = self.carter.say(input_text, player_id)

    def test_unconvertible_text_valid_player_id(self):
        input_text = TestCarter.UnconvertibleToString()
        player_id = "12345"

        with self.assertRaises(TypeError):
            interaction = self.carter.say(input_text, player_id)

    def test_unconvertible_text_unconvertible_player_id(self):
        input_text = TestCarter.UnconvertibleToString()
        player_id = TestCarter.UnconvertibleToString()

        with self.assertRaises(TypeError):
            interaction = self.carter.say(input_text, player_id)


if __name__ == '__main__':
    logging.basicConfig( stream=sys.stderr )
    logging.getLogger( "SomeTest.testSomething" ).setLevel( logging.DEBUG )
    unittest.main(buffer=False)
