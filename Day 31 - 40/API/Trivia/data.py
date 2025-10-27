import requests as rq

API = "https://opentdb.com/api.php?amount=10&type=boolean"
question_data = []


response = rq.get(url=API)
response.raise_for_status()
data = response.json()
results = data["results"]

for item in results:
    question = item["question"]
    answer = item["correct_answer"]
    category = item["category"]

    question_data.append({
        "question": question,
        "answer": answer,
        "category": category
    })

print(question_data)

