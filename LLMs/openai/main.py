from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()
client = OpenAI()

response = client.responses.create(
    model="gpt-4o-mini",
    input="give me a word start with letter P"
)

print(response.output_text)