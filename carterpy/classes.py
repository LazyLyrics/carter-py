import uuid

class Interaction():
    def __init__(self, payload, response, time_taken):
        carter_data = response.json()
        # Carter data
        self.input_text = payload['text']
        self.output_text = carter_data['output']['text'] if response.ok else None
        self.forced_behaviours = carter_data['forced_behaviours'] if response.ok else None

        # carter-py data
        self.id = uuid.uuid1()
        self.ok = response.ok
        self.response = response
        self.status_code = response.status_code
        self.status_message = response.reason
        self.triggered_skills = []
        self.executed_skills = []
        self.time_taken = time_taken

    def __str__(self):
        if self.response.ok:
            return f"Interaction {self.id} - {self.input_text} -> {self.output_text}"
        else:
            return f"Interaction {self.id} - Failed with status code {self.status_code} and message {self.status_message}"
