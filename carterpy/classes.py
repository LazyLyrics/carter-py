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

        # set response params
        if response_data is not None:
            self.ok = response_data["ok"]
            self.status_code = response_data["status_code"]
            self.status_message = response_data["status_message"]
            carter_data = response_data["carter_data"]
            if carter_data is not None:
                if "output" in carter_data:
                    self.output_text = carter_data["output"]["text"]
                    self.output_audio = carter_data["output"]["audio"]
                else:
                    self.output_text = None
                    self.output_audio = None

                if "content" in carter_data:
                    self.output_text = carter_data["content"]
                if "sentence" in carter_data:
                    self.output_text = carter_data["sentence"]
                if "output_text" not in self.__dict__:
                    self.output_text = None


                if "forced_behaviours" in carter_data:
                    self.forced_behaviours = carter_data["forced_behaviours"]
                else:
                    self.forced_behaviours = None
            else:
                self.ok = False
                self.output_text = None
                self.forced_behaviours = None

        else:
            self.ok = False
            self.status_code = None
            self.status_message = None
            self.output_text = None
            self.forced_behaviours = None

        # Payload data
        if "text" in self.payload:
            self.input_text = self.payload["text"]
        else:
            self.input_text = self.type

        if "player_id" in self.payload:
            self.player_id = self.payload["player_id"]
        else:
            self.player_id = None

    def __str__(self):
        if self.ok:
            return f"{self.type.capitalize()} interaction {self.id} - {self.input_text} -> {self.output_text}"
        else:
            return f"{self.type.capitalize()} interaction {self.id} - Failed with status code {self.status_code} and message {self.status_message}"

    def print_verbose(self):
        for key, value in self.__dict__.items():
            print("=====================================")
            print(f"{self.type.upper()} INTERACTION {self.id}")
            print(f"{key}: {value}")
            print("=====================================")
