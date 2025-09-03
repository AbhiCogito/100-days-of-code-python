import os
import pandas as pd 
os.system("clear")
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "nato_phonetic_alphabet.csv")
os.system("clear")

df = pd.DataFrame(pd.read_csv(file_path))

db = {column["letter"]:column["code"] for index, column in df.iterrows()}
# print(db.values())

word = input("Enter the word for phonics conversion: ").upper()
# print(word)

try:
    result = [db[w] for w in word]
except KeyError:
    print("Only alphabets.")
else:
    print(result)


# r = []

# for w in word:
#     if w in db:
#         r.append(db[w])

# result = [k for k in db.values() if (for w in word) == db.keys()]
# result = [phonics for list(word) in db.values()]

# result = {a,b for a,b in db.values() if list(word) in db.keys()}
# print(result)

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

