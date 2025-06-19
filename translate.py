import openai
import os

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

Gazan_prompt = """
Translate the following text between English and Gazan Arabic.

When input is English, output Gazan Arabic.  
When input is Arabic (Gazan), output English.

Input: "{text}"
Output:"""

def translate(text: str) -> str:
    prompt = Gazan_prompt.format(text=text)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a Gazan Arabic translator."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=60,
    )
    return response.choices[0].message.content.strip()
