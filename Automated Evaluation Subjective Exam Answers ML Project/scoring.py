from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def evaluate_answers(student_answers, answer_key, rubric):
    scores = []

    for idx, student_ans in enumerate(student_answers):
        ref_ans = answer_key[idx]
        key_points = rubric[str(idx + 1)]["key_points"]
        max_score = rubric[str(idx + 1)]["max_score"]

        # Semantic similarity score
        emb1 = model.encode(student_ans, convert_to_tensor=True)
        emb2 = model.encode(ref_ans, convert_to_tensor=True)
        semantic_score = util.pytorch_cos_sim(emb1, emb2).item()

        # Rubric matching score
        matched_points = sum(1 for point in key_points if point.lower() in student_ans.lower())
        rubric_score = matched_points / len(key_points)

        # Hybrid score
        final_score = (semantic_score * 0.4 + rubric_score * 0.6) * max_score
        scores.append(round(min(final_score, max_score), 2))

    return scores





