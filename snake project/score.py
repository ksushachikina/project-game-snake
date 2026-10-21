import json

HIGH_SCORE = "highscore.json"

def find_score():
    try:
        with open(HIGH_SCORE, encoding="utf8") as file:
            score = json.load(file)
        return max(int(score["high_score"]), 0)
    except:
        return 0

def save_score(score):
    with open(HIGH_SCORE, "w", encoding="utf8") as file:
        json.dump({"high_score": score}, file)
