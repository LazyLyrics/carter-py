import uuid
from .utils import iso_now
import uuid
from .utils import iso_now


class Interaction():
    def __init__(self, type, payload, response_data, time_taken):

        # set easy stuff
        self.type = type
        self.id = uuid.uuid1()
        self.payload = payload
        self.time_taken = time_taken
        self.timestamp = iso_now()
        self.triggered_skills = []
        self.executed_skills = []
        self.carter_data = response_data["carter_data"] if response_data is not None else None
        self.url = response_data["url"] if response_data is not None else None

        # set params from response_data
        if response_data is not None:
            self.ok = response_data["ok"]
            self.status_code = response_data["status_code"]
            self.status_message = response_data["status_message"]
            carter_data = response_data["carter_data"]

            if carter_data is not None:
                # Process output text and audio
                output = carter_data.get("output")
                if output:
                    self.output_text = output.get("text")
                    self.output_audio = output.get("audio") if "audio" in output else None
                else:
                    self.output_text = None
                    self.output_audio = None

                # Process content, sentence, and forced_behaviours
                self.output_text = carter_data.get("content") or carter_data.get("sentence") or self.output_text
                self.forced_behaviours = carter_data.get("forced_behaviours") or None
            else:
                self.ok = False
                self.output_text = None
                self.forced_behaviours = None

        # If no response
        else:
            self.ok = False
            self.status_code = None
            self.status_message = None
            self.output_text = None
            self.forced_behaviours = None

        # Payload data
        self.input_text = self.payload.get("text", self.type)
        self.player_id = self.payload.get("player_id")


    def __str__(self):
        if self.ok:
            return f"<{self.type.capitalize()} interaction {self.id} - {self.input_text} -> {self.output_text}>"
        else:
            return f"<{self.type.capitalize()} interaction {self.id} - Failed with status code {self.status_code} and message {self.status_message}>"

    def print_verbose(self):
        print("=====================================")
        print(f"{self.type.upper()} INTERACTION {self.id}")
        for key, value in self.__dict__.items():
            print(f"{key}: {value}")
        print("=====================================")
