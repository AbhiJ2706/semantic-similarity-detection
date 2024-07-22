import os
from openai import OpenAI


class InputProvider:

    def provide(self, **kwargs):
        raise NotImplementedError("Not Implemented")


class StandardInputProvider(InputProvider):

    def provide(self, **kwargs):
        return input("Enter paragraph:\n")


class FileInputProvider(InputProvider):

    def provide(self, **kwargs):
        with kwargs["file"] as f:
            return f.read()


class ChatGPTInputProvider(InputProvider):

    def __init__(self):
        try:
            self.api_key = os.environ["API_KEY"]
        except:
            raise Exception("OpenAI API key not present at $API_KEY.")

        self.client = OpenAI(
            api_key=self.api_key
        )
    
    def provide(self, **kwargs):
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": kwargs["prompt"]},
            ]
        )
        return response.choices[0].message.content