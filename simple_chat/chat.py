import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPEN_AI_KEY"))

message = input("What's on your mind today?\n")
while(message!=""):
    response = client.responses.create(
        model="gpt-5-nano",
        input=message,
        text={"verbosity":"low"}
    )
    print(response.output_text)
    message=input("")
