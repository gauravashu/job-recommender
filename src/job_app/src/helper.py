
import pymupdf
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=GROQ_API_KEY)


def extract_text_from_pdf(uploaded_file):
    """
    Extracts text from a PDF file.

    Args:
        uploaded_file: Uploaded PDF file.

    Returns:
        str: The extracted text.
    """
    doc = pymupdf.open(
        stream=uploaded_file.read(),
        filetype="pdf"
    )

    text = ""

    for page in doc:
        text += page.get_text()

    doc.close()

    return text


def ask_openai(prompt, max_tokens=500):
    """
    Sends a prompt to the Groq API and returns the response.
    The function name is kept as ask_openai so app.py
    does not need to be changed.
    """

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=max_tokens
    )

    return response.choices[0].message.content
