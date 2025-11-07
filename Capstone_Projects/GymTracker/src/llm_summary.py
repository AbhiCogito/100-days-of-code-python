import requests, sys, os, json
from dotenv import load_dotenv
from analysis.summary import progress_data

load_dotenv()
os.system("clear")

GROQ_API = os.getenv("GROQ_LLM_API")
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

MAX_LENGTH = 5000  
short_progress_data = str(progress_data)[:MAX_LENGTH]

# Format prompt
prompt = f"Analyze this workout progress data and give insights, trends, and suggestions:\n{short_progress_data}"

# Groq API call
url = "https://api.groq.com/openai/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {GROQ_API}",
    "Content-Type": "application/json"
}
payload = {
    "model": "qwen/qwen3-32b",  # You can also try llama3-8b-8192 or gemma-7b-it
    "messages": [
        {"role": "user", "content": prompt}
    ]
}

response = requests.post(url, headers=headers, json=payload)

# Check if the response contains the 'choices' key
response_data = response.json()

if response.status_code == 200:
    #Most LLMs return a JSON which contains <choices> dictionary. Its presence means response is successful.
    if "choices" in response_data:
        # print(json.dumps(response_data, indent=2)) #To check for tokwn usage
        llm_response = response_data["choices"][0]["message"]["content"] #To print only the text output from the model
    else:
        print("No 'choices' key found in the response. Here's the full response:")
        print(response_data)
else:
    print(f"Error: {response.status_code}")
    llm_response = response_data