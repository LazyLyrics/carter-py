# `carterpy`: A Python Wrapper for the Carter API

`carterpy` is a Python package that provides a simple wrapper for the Carter API. It allows you to easily send text messages to the API and receive responses with minimal setup, and with the ability to add more complex functionality in upcoming releases.

## Installation

To install `carterpy`, you can use pip, Python's package manager. Simply run the following command:

```bash
pip install `carterpy`
```

This will install the latest version of `carterpy` and its dependencies.

## Usage

To use `carterpy`, you will need to obtain an API key from the Carter website. Once you have your API key, you can use it to create a Carter object and start sending messages. Here's an example:

```python

from `carterpy` import Carter


# Replace YOUR_API_KEY with your actual API key

carter = Carter("YOUR_API_KEY")

# Send a message to the API

response = carter.say("Hello, world!", "player123")

# Print the response text

print(response.output_text)

```

`carter.say()` returns an instance of the Interaction class, which contains the response text and other information about the interaction. It takes input text, and optionally a player ID, as arguments. If you don't specify a player ID, it will use a random one. Both must be strings or convertible to strings.

```text
class Interaction():
    # Represents a single interaction with the Carter API.
    input_text (str): The input text that was sent to the API.
    output_text (str): The output text that was received from the API.
    forced_behaviours (array): The forced behaviours that were applied by the API.
    id (uuid.UUID): The unique identifier of the interaction.
    ok (bool): Whether the response was successful or not.
    response (requests.Response): The response object returned by the API.
    status_code (int): The status code of the response.
    status_message (str): The status message of the response.
    time_taken (int): The time taken to receive the response, in milliseconds.
    timestamp (string): The timestamp of the interaction in isoformat.
```

## Opener

Make use of the `/opener` endpoint to get a random opener from the Carter API. This is useful for when you want to start a conversation with a player.

```python
# with carter object already created

interaction = carter.opener("player123")
print(interaction.output_text)
```

```text
class OpenerInteraction():
    # Represents a single opener interaction with the Carter API.
    output_text (str): The output text that was received from the API.
    id (uuid.UUID): The unique identifier of the interaction.
    ok (bool): Whether the response was successful or not.
    response (requests.Response): The response object returned by the API.
    status_code (int): The status code of the response.
    status_message (str): The status message of the response.
    time_taken (int): The time taken to receive the response, in milliseconds.
    timestamp (string): The timestamp of the interaction in isoformat.
```

## Personalise

Make use of the `/personalise` endpoint to personalise any text in the style of your Carter character.

```python
# with carter object already created

interaction = carter.personalise("Hello, world!")
print(interaction.output_text)
```

```text
class PersonaliseInteraction():
    # Represents a single personalise interaction with the Carter API.
    output_text (str): The output text that was received from the API.
    id (uuid.UUID): The unique identifier of the interaction.
    ok (bool): Whether the response was successful or not.
    response (requests.Response): The response object returned by the API.
    status_code (int): The status code of the response.
    status_message (str): The status message of the response.
    time_taken (int): The time taken to receive the response, in milliseconds.
    timestamp (string): The timestamp of the interaction in isoformat.
```

## History

Each successful interaction with your character is stored in `Carter.history`. This is a list of Interaction objects with the most recent first. You can use this to keep track of the interactions that have taken place.

```python
# with carter object already created

carter.say("Hello, world!", "player123")
carter.say("How are you?", "player123")

print(carter.history[0].input_text)
print(carter.history[1].input_text)

# Output:
# How are you?
# Hello, world!
```

## Upcoming features

- Soon you'll be able to register skills with your agent, this will allow you to trigger functions in your code when `carterpy` detects forced behaviours in the response. This could trigger some other functionality in your code, and even customise the response to add extra data.
- Improved logging, including the ability to pass your logger to the `Carter` object for debugging.

## `carterjs`

`carterpy` is a Python wrapper for the Carter API. If you're looking for a JavaScript wrapper, check out [`carterjs`](https://github.com/LazyLyrics/carter-js)

## Contributing

If you would like to contribute to `carterpy`, you can do so by opening an issue or pull request on the GitHub repository.
