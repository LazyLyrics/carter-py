import datetime

URLS = {
    "say": "https://unstable.carterlabs.ai/api/say",
    "opener": "https://unstable.carterlabs.ai/api/opener",
    "personalise": "https://unstable.carterlabs.ai/api/personalise",
}

def convert_to_string(variable_name, value):
    try:
        return str(value)
    except:
        raise TypeError(f"{variable_name} must be convertible to a string, received {type(value)}")

def iso_now():
    return datetime.datetime.now().isoformat()
