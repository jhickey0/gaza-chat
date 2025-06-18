import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

Gazan_prompt = """
Translate the following text between English and Gazan Arabic.

When input is English, output Gazan Arabic.  
When input is Arabic (Gazan), output English.

Input: "{text}"
Output:"""

def translate(text: str) -> str:
    prompt = Gazan_prompt.format(text=text)
    resp = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=60,
        temperature=0.7,
    )
    return resp.choices[0].text.strip()
