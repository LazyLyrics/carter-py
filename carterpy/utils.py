import datetime

URLS = {
    "say": "https://api.carterlabs.ai/api/chat",
    "opener": "https://api.carterlabs.ai/api/opener",
    "personalise": "https://api.carterlabs.ai/api/personalise",
}

def convert_to_string(variable_name, value):
    try:
        return str(value)
    except:
        raise TypeError(f"{variable_name} must be convertible to a string, received {type(value)}")

def iso_now():
    return datetime.datetime.now().isoformat()
