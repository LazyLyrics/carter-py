# `carterpy`: A Python Wrapper for the Carter API

`carterpy` is a Python package that provides a simple wrapper for the Carter API. It allows you to easily send text messages to the API and receive responses.

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

`carter.say()` returns an instance of the Interaction class, which contains the response text and other information about the interaction.

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
```

This code will create a Carter object with your API key, and use it to send a message to the API. The response will be stored in the response variable, and you can access the response text using the output_text attribute.

## Contributing

If you would like to contribute to `carterpy`, you can do so by opening an issue or pull request on the GitHub repository.
