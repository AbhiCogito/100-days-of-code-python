import requests
import datetime

import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from analysis.summary import progress_data

print(progress_data)

# # Format prompt
# prompt = f"Analyze this workout progress data and give insights, trends, and suggestions:\n{progress_data}"

# # Groq API call
# url = "https://api.groq.com/openai/v1/chat/completions"
# headers = {
#     "Authorization": "Bearer YOUR_GROQ_API_KEY",
#     "Content-Type": "application/json"
# }
# payload = {
#     "model": "mixtral-8x7b-32768",  # You can also try llama3-8b-8192 or gemma-7b-it
#     "messages": [
#         {"role": "user", "content": prompt}
#     ]
# }

# response = requests.post(url, headers=headers, json=payload)
# print(response.json()["choices"][0]["message"]["content"])
