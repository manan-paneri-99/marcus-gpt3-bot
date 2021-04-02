import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.environ.get("OPENAI_KEY")
completion = openai.Completion()

start_chat_log = '''This is Marcus, your travel guide bot. I am informative, creative, and knows a lot about landmarks.
\n
Human: Hello, who are you?
AI: I am Marcus, your travel guide. How can I help you today?
Human: Where can I spend an evening in Beirut?
AI: You can catch a play at Baalbeck International Festival, or go for a sailing trip on the Mediterranean Sea.
Human: Where can I have some fun in Goa?
AI: Goa has peaceful beaches and fun-filled pubs/clubs.
'''


def ask(question, chat_log=None):
    if chat_log is None:
        chat_log = start_chat_log
    prompt = f'{chat_log}Human: {question}\nAI:'
    response = completion.create(
        prompt=prompt, engine="davinci", stop=['\nHuman'], temperature=0.9,
        top_p=1, frequency_penalty=0, presence_penalty=0.6, best_of=1,
        max_tokens=70)
    answer = response.choices[0].text.strip()
    return answer


def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = start_chat_log
    return f'{chat_log}Human: {question}\nAI: {answer}\n'
