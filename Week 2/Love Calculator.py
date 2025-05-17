import os
os.system("clear")

def calculate_love_score(name1, name2):
    true = "true"
    love = "love"
    name = (name1 + name2).lower() #lovesophie
    score1 = 0
    score2 = 0
    for x in true:
        for y in name:
            if x == y:
                score1 += 1

    for x in love:
        for y in name:
            if x == y:
                score2 += 1
    return(score1, score2)

score1, score2 = calculate_love_score("Kanye West", "Kim Kardashian")
print(f"Your score is {score1}{score2}")
