import json
import os
from extract_text import extract_student_answers
from scoring import evaluate_answers
from utils import load_answer_key, load_rubric

# Load rubric and key
answer_key = load_answer_key("data/answer_key.txt")
rubric = load_rubric("data/rubric.json")

# Use uploaded PDF
pdf_path = "data/students/qna[1].pdf"
student_answers = extract_student_answers(pdf_path)

# Evaluate
scores = evaluate_answers(student_answers, answer_key, rubric)

# Output
print("\nEvaluation Results:")
total = 0
for idx, score in enumerate(scores, 1):
    print(f"Q{idx}: {score}/{rubric[str(idx)]['max_score']}")
    total += score
print(f" Total Score: {total}/{sum(r['max_score'] for r in rubric.values())}")

output_dir = "data/outputs"
os.makedirs(output_dir, exist_ok=True)

output_path = os.path.join(output_dir, "qna_scores.json")
with open(output_path, "w") as f:
    json.dump(scores, f, indent=2)
