# carter-py: A Python Wrapper for the Carter API

[GitHub](https://github.com/LazyLyrics/carter-py) | [PyPI](https://pypi.org/project/carter-py/) | [Change Log](https://github.com/LazyLyrics/carter-py/blob/main/CHANGELOG.md)| [Docs](https://lazylyrics.gitbook.io/carter-py-v1/)

`carter-py` is a Python package that provides a simple wrapper for the Carter API. It allows you to easily send text messages to the API and receive responses with minimal setup, and with the ability to add more complex functionality in upcoming releases.

Please note that this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html). As carter-py is built around an API which is still in beta, breaking changes may be introduced indirectly in minor releases. Major releases will be reserved for breaking changes to the way in carter-py is used. IE. function names, parameter depreciations etc. Where a breaking change is made on the API side, carter-py will be updated to reflect this change.

I will continue to build carter-py with the intention of maintaining backwards compatibility, but this is not guaranteed. Previous versions of carter-py are always likely to be outdated as the API progresses. Please consult the changelog for any breaking changes and try to use the latest version of carter-py.

## Installation

```bash
pip install `carter-py`
```

This will install the latest version of `carter-py` and its dependencies.

**Note**: `carter-py` has two classes, a Carter class and an AsyncCarter class. The AsyncCarter class is used for asynchronous usage of the API. The Carter class is used for synchronous usage of the API. An example of asynchronous usage can be found below.

## Usage

To use `carter-py`, you will need to obtain an API key from the Carter website. Once you have your API key, you can use it to create a Carter object and start sending messages. Here's an example:

```python

from `carterpy` import Carter


# Replace YOUR_API_KEY with your actual API key

carter = Carter("YOUR_API_KEY")

# Send a message to the API

response = carter.say("Hello, world!", "player123")

# Print the response text

print(response.output_text)

```

`carter.say()` returns an instance of the Interaction class, which contains the response text and other information about the interaction. It takes input text, and optionally a user_id, as arguments. If you don't specify a player ID, it will use a random one. Both must be strings or convertible to strings.

### Opener

Make use of the `/opener` endpoint to get a random opener from the Carter API. This is useful for when you want to start a conversation with a player.

```python
# with carter object already created

interaction = carter.opener("player123")
print(interaction.output_text)
```

### Personalise

Make use of the `/personalise` endpoint to personalise any text in the style of your Carter character.

```python
# with carter object already created

interaction = carter.personalise("Hello, world!", "player_id")
print(interaction.output_text)
```

### Speak

When using any of the methods above, the output audio will **not** be returned by default as this currently introduces significant latency on the API end. If you want to receive the audio you have two options. You can set the `speak` parameter to `True` when creating the Carter object, or you can set it to `True` when calling the method. When calling a function `carter-py` will check to see if you have provided a speak parameter, if you have then it will override the default on the class. If you have not provided a speak parameter, then it will use the default on the class. Here's an example:

```python
    carter = Carter('your-api-key') # False by default

    interaction = carter.say("Hello, world!", "player123") # No audio will be returned, because you have not overridden the default on the class

    interaction = carter.say("Hello, world!", "player123", speak=True) # Audio will be returned, because you have overridden the default on the class
```

### Interactions

Each request to carter returns an instance of the Interaction class. This contains information about the interaction, including the input text, output text, and forced behaviours. It also contains the status code and message, and the time taken to receive the response. Both the `opener()` and `personalise()` methods return an Interaction object, with the redundant properties removed. Here's an example of the Interaction class:

```text
# Represents a single interaction with the Carter API.

class Interaction():
    input_text (str): The input text that was sent to the API. # Not present in opener()
    output_text (str): The output text that was received from the API.
    output_audio (str): The output audio url that was received from the API (only if speak is True)
    forced_behaviours (array): The forced behaviours that were applied by the API. # Not present in opener() or personalise()
    id (uuid.UUID): The unique identifier of the interaction.
    time_taken (int): The time taken to receive the response, in milliseconds.
    timestamp (string): The timestamp of the interaction in isoformat.
    ok (bool): Whether the response was successful or not.
    status_code (int): The status code of the response.
    status_message (str): The status message of the response.
```

Some properties may be None if the interaction was not successful. Always check the `ok` property before using the other properties, if there was an error with `carter-py` then all data related to output (`output_text, output_audio, forced_behaviours, status_code, status_message`) will be `None`. If there was an error with the API, then the `ok` property will be `False` and the `status_code` and `status_message` properties will be populated with the error information, but output data will still be None.

### History

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

### Upcoming features

- Soon you'll be able to register skills with your agent, this will allow you to trigger functions in your code when `carter-py` detects forced behaviours in the response. This could trigger some other functionality in your code, and even customise the response to add extra data.
- Improved logging, including the ability to pass your logger to the `Carter` object for debugging.

### carter-js

`carter-py` is a Python wrapper for the Carter API. If you're looking for a JavaScript wrapper, check out [`carter-js`](https://github.com/LazyLyrics/carter-js)

### Contributing

If you would like to contribute to `carter-py`, you can do so by opening an issue or pull request on the GitHub repository.

## Asynchronous Usage

```python
import asyncio
from carterpy import AsyncCarter

# Replace YOUR_API_KEY with your actual API key
api_key = "YOUR_API_KEY"

async def main():
    async_carter = AsyncCarter(api_key)

    # with carter object already created
    interaction = await async_carter.say("hi there!", "player123")
    personalise = await async_carter.personalise("Hello, world!")
    opener = await async_carter.opener("player123")
    print(interaction.output_text)

asyncio.run(main())
```

Once the initial interaction is created, all of the properties of the interaction are available to use. For example, you can use `interaction.output_text` to get the output text of the interaction.
