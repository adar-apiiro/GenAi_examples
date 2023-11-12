import openai, numpy as np, pandas as pd, re
from tqdm import tqdm
openai.api_key = 
model_engine = "gpt-4"

def rollChatGPT(prompt):
    completion = openai.ChatCompletion.create(
    model=model_engine,
    messages=[{"role": "system", "content":"This is the year 2099.I am a cyberpunk AI. Ask me anything."},\
              {'role': 'user', 'content': prompt}],
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5)

    return completion.choices[0]['message']['content'], completion
