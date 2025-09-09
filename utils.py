import json

def load_answer_key(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return [q.strip() for q in f.read().split("Answer ")[1:]]

def load_rubric(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

